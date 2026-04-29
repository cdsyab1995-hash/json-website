// Google AdSense - adsbygoogle.js
// Replace 'ca-pub-XXXXXXXXXXXXXXXX' with your actual AdSense Publisher ID
// after your site is approved for Google AdSense

(function() {
  // Your AdSense Publisher ID (replace after approval)
  var ADSENSE_PUB_ID = 'ca-pub-XXXXXXXXXXXXXXXX';
  
  // Check if ads should be loaded (can be disabled via query param)
  var disableAds = new URLSearchParams(window.location.search).get('noads') === '1';
  
  if (!disableAds && ADSENSE_PUB_ID.indexOf('XXXXXXXX') === -1) {
    // Load adsbygoogle script
    var script = document.createElement('script');
    script.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' + ADSENSE_PUB_ID;
    script.setAttribute('crossorigin', 'anonymous');
    script.async = true;
    document.head.appendChild(script);
    
    // Define adsbygoogle after script loads
    window.adsbygoogle = window.adsbygoogle || [];
    window.adsbygoogle.push({
      google_ad_client: ADSENSE_PUB_ID,
      enable_page_level_ads: true
    });
  }
})();
