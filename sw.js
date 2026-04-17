// Service Worker for JSON Tools PWA
// Version: 1.0.0

const CACHE_VERSION = 'v1';
const CACHE_NAME = `json-tools-${CACHE_VERSION}`;
const STATIC_CACHE = `json-tools-static-${CACHE_VERSION}`;
const DYNAMIC_CACHE = `json-tools-dynamic-${CACHE_VERSION}`;

// Core static assets to cache immediately
const STATIC_ASSETS = [
    '/',
    '/index.html',
    '/css/styles.css',
    '/js/app.js',
    '/images/favicon.svg',
    '/images/icon-192.png',
    '/images/icon-512.png',
    // Tool pages
    '/pages/format.html',
    '/pages/escape.html',
    '/pages/extract.html',
    '/pages/sort.html',
    '/pages/clean.html',
    '/pages/xml.html',
    '/pages/yaml.html',
    '/pages/viewer.html',
    '/pages/json2csv.html',
    '/pages/compare.html',
    '/pages/regex-tester.html',
    '/pages/base64.html',
    '/pages/url-encoder.html',
    '/pages/jwt-decoder.html',
    '/pages/hash-generator.html',
    '/pages/uuid-generator.html',
    '/pages/timestamp-converter.html',
    '/pages/merge-csv.html',
    '/pages/batch-file-renamer.html',
    '/pages/pdf-split.html',
    '/pages/css-minifier.html',
    '/pages/html-encoder.html',
    '/pages/blog.html',
    '/pages/best-practices.html',
    '/pages/news.html',
    '/pages/about.html',
    '/pages/changelog.html',
];

// Install event - cache static assets
self.addEventListener('install', (event) => {
    console.log('[SW] Installing...');
    event.waitUntil(
        caches.open(STATIC_CACHE).then((cache) => {
            console.log('[SW] Caching static assets');
            // Cache assets in batches, ignore failures
            const cachePromises = STATIC_ASSETS.map(url => 
                cache.add(url).catch(err => console.warn(`[SW] Failed to cache ${url}:`, err))
            );
            return Promise.all(cachePromises);
        }).then(() => {
            console.log('[SW] Installation complete');
            return self.skipWaiting();
        })
    );
});

// Activate event - clean old caches
self.addEventListener('activate', (event) => {
    console.log('[SW] Activating...');
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames
                    .filter(name => name.startsWith('json-tools-') && name !== STATIC_CACHE && name !== DYNAMIC_CACHE)
                    .map(name => {
                        console.log('[SW] Deleting old cache:', name);
                        return caches.delete(name);
                    })
            );
        }).then(() => {
            console.log('[SW] Activation complete');
            return self.clients.claim();
        })
    );
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', (event) => {
    // Only handle GET requests
    if (event.request.method !== 'GET') return;
    
    const url = new URL(event.request.url);
    
    // Don't cache external requests (fonts, etc.)
    if (url.hostname !== self.location.hostname && 
        !url.hostname.includes('fonts.gstatic.com') &&
        !url.hostname.includes('fonts.googleapis.com')) {
        return;
    }
    
    event.respondWith(
        caches.match(event.request).then((cachedResponse) => {
            // Return cached version if available
            if (cachedResponse) {
                // Update cache in background (stale-while-revalidate)
                const fetchPromise = fetch(event.request).then((networkResponse) => {
                    if (networkResponse && networkResponse.status === 200) {
                        const cacheName = STATIC_ASSETS.includes(url.pathname) ? STATIC_CACHE : DYNAMIC_CACHE;
                        caches.open(cacheName).then((cache) => {
                            cache.put(event.request, networkResponse.clone());
                        });
                    }
                    return networkResponse;
                }).catch(() => null);
                
                return cachedResponse;
            }
            
            // Fetch from network and cache
            return fetch(event.request).then((networkResponse) => {
                if (!networkResponse || networkResponse.status !== 200) {
                    return networkResponse;
                }
                
                const responseToCache = networkResponse.clone();
                caches.open(DYNAMIC_CACHE).then((cache) => {
                    cache.put(event.request, responseToCache);
                });
                
                return networkResponse;
            }).catch(() => {
                // Fallback for offline HTML requests
                if (event.request.headers.get('accept').includes('text/html')) {
                    return caches.match('/offline.html') || caches.match('/index.html');
                }
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
    console.log('[SW] Syncing analytics...');
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
