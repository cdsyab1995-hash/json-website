// Service Worker for JSON Tools PWA
// Version: 1.0.0

const CACHE_VERSION = 'v2';
const CACHE_NAME = `json-tools-${CACHE_VERSION}`;
const STATIC_CACHE = `json-tools-static-${CACHE_VERSION}`;
const DYNAMIC_CACHE = `json-tools-dynamic-${CACHE_VERSION}`;

// Core static assets to cache immediately (no HTML pages - always served from network)
const STATIC_ASSETS = [
    '/',
    '/index.html',
    '/css/styles.css',
    '/js/app.js',
    '/js/navbar.js',
    '/images/favicon.svg',
    '/images/icon-192.png',
    '/images/icon-512.png',
    '/images/apple-touch-icon.png',
    '/manifest.json',
];

// Install event - cache static assets
self.addEventListener('install', (event) => {
    // console statement removed
    event.waitUntil(
        caches.open(STATIC_CACHE).then((cache) => {
            // console statement removed
            // Cache assets in batches, ignore failures
            const cachePromises = STATIC_ASSETS.map(url => 
                cache.add(url).catch(err => console.warn(`[SW] Failed to cache ${url}:`, err))
            );
            return Promise.all(cachePromises);
        }).then(() => {
            // console statement removed
            return self.skipWaiting();
        })
    );
});

// Activate event - clean old caches
self.addEventListener('activate', (event) => {
    // console statement removed
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames
                    .filter(name => name.startsWith('json-tools-') && name !== STATIC_CACHE && name !== DYNAMIC_CACHE)
                    .map(name => {
                        // console statement removed
                        return caches.delete(name);
                    })
            );
        }).then(() => {
            // console statement removed
            return self.clients.claim();
        })
    );
});

// Fetch event - HTML pages always go to network; static assets use cache-first
self.addEventListener('fetch', (event) => {
    // Only handle GET requests
    if (event.request.method !== 'GET') return;
    
    const url = new URL(event.request.url);
    
    // Don't handle external requests (fonts, analytics, etc.)
    if (url.hostname !== self.location.hostname) return;
    
    const pathname = url.pathname;
    
    // CRITICAL: Always fetch HTML pages from network (no SW caching for HTML)
    // This prevents serving stale cached pages and ensures proper MIME types
    if (pathname.endsWith('.html') || pathname.endsWith('/')) {
        event.respondWith(
            fetch(event.request).catch(() => {
                // Fallback for offline HTML requests
                if (event.request.headers.get('accept').includes('text/html')) {
                    return caches.match('/index.html');
                }
            })
        );
        return;
    }
    
    // Static assets (CSS, JS, images) use cache-first strategy
    event.respondWith(
        caches.match(event.request).then((cachedResponse) => {
            if (cachedResponse) {
                // Update cache in background (stale-while-revalidate)
                fetch(event.request).then((networkResponse) => {
                    if (networkResponse && networkResponse.status === 200) {
                        caches.open(STATIC_CACHE).then((cache) => {
                            cache.put(event.request, networkResponse.clone());
                        });
                    }
                }).catch(() => {});
                return cachedResponse;
            }
            
            // Fetch from network and cache static assets
            return fetch(event.request).then((networkResponse) => {
                if (!networkResponse || networkResponse.status !== 200) {
                    return networkResponse;
                }
                const responseToCache = networkResponse.clone();
                caches.open(STATIC_CACHE).then((cache) => {
                    cache.put(event.request, responseToCache);
                });
                return networkResponse;
            });
        })
    );
});

// Background sync for analytics
self.addEventListener('sync', (event) => {
    if (event.tag === 'sync-analytics') {
        event.waitUntil(syncAnalytics());
    }
});

async function syncAnalytics() {
    // Placeholder for analytics sync
    // console statement removed
}

// Push notifications (future use)
self.addEventListener('push', (event) => {
    if (event.data) {
        const data = event.data.json();
        const options = {
            body: data.body,
            icon: '/images/icon-192.png',
            badge: '/images/icon-96.png',
            data: { url: data.url || '/' }
        };
        event.waitUntil(
            self.registration.showNotification(data.title, options)
        );
    }
});

self.addEventListener('notificationclick', (event) => {
    event.notification.close();
    event.waitUntil(
        clients.openWindow(event.notification.data.url)
    );
});
