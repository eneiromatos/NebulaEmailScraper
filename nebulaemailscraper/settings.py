# Scrapy settings for nebulaemailscraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "nebulaemailscraper"

SPIDER_MODULES = ["nebulaemailscraper.spiders"]
NEWSPIDER_MODULE = "nebulaemailscraper.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'nebulaemailscraper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "authority": "www.google.com",
    "cache-control": "max-age=0",
    "sec-ch-dpr": "1",
    "sec-ch-viewport-width": "1366",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-full-version": '"99.0.4844.82"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"10.0.0"',
    "sec-ch-ua-model": '""',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version-list": '" Not A;Brand";v="99.0.0.0", "Chromium";v="99.0.4844.82", "Google Chrome";v="99.0.4844.82"',
    "dnt": "1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-client-data": "CJe2yQEIpbbJAQjEtskBCKmdygEInOzKAQiVocsBCJ75ywEI54TMAQiljswBCPiqzAEI6qvMARirqcoB",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "accept-language": "es-ES,es;q=0.9,en;q=0.8,pt;q=0.7",
    "cookie": "1P_JAR=2022-04-30-07; AEC=AakniGOTtR31N-sez3RQr7c9wCSVHT59jP6l5DpdLaybNlxfCoaPJXJDzyM; SID=JwjWn6xu-tHXDKRbECXPuJobRp1Koi1vUc_dJlRUm4sd4KBYj5exA8ZQpK1ZDkMvdD8q7Q.; __Secure-1PSID=JwjWn6xu-tHXDKRbECXPuJobRp1Koi1vUc_dJlRUm4sd4KBYVbDpJ7BqRPAgpGcDIrg3Uw.; __Secure-3PSID=JwjWn6xu-tHXDKRbECXPuJobRp1Koi1vUc_dJlRUm4sd4KBYotsYsqaHwGoKy40G9n4S8A.; HSID=AdTglgs-tyAfM63mi; SSID=AdPHPWLzNpQs6iP5M; APISID=eG0_b2qJluodbrwH/AS7mqV0MfqoN_99Tz; SAPISID=ruVwVaHCumXA3agj/ArKiOvu36UpDhIquQ; __Secure-1PAPISID=ruVwVaHCumXA3agj/ArKiOvu36UpDhIquQ; __Secure-3PAPISID=ruVwVaHCumXA3agj/ArKiOvu36UpDhIquQ; NID=511=CJ2RlqsIsA30-jxsKpdphkOY453ujH9i2a55lIpEitBk14hYP8830jwVtnZJrdW-J6qcLIMh2GFCGwvX55xYs3Ci_UBYvbzhqaWpv_xuMj6CztDzPkaCthQ9xn9EqExCJi685A5XP_gjssFXLLoHziE06w4crOsTybKj2XU77XI_pSk4XRuBIJcytNHtq9c7EsBhyfu2Mel6T6p4MT6bkCeNUd7klxeZqYn8hvWhooNLeDzFm5oS1iDLP3viTcMh29Vjp2JccNGcYgAbjgc_WcgZ79jMg1MHJDCjxF8oMw; DV=ExmPqzBraHo7kBavBNZ2oiEtXiKVBxgijpdIBVqZBvjGAICPDvztW_cmCwaFAAA; SIDCC=AJi4QfHnEMrDGi_f3s2hOd6DgCl6RrJNFXQGOp6U3tF-87mNhfJGdZBs8j7d0CVWhtsnJ22m; __Secure-3PSIDCC=AJi4QfFju6lmkwdN-JkSwdrg82Q7r67dsh6cFiSp6qkTFvcHNaq-y7fbsxTkHLPfvCKgBTxnkw",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'nebulaemailscraper.middlewares.NebulaemailscraperSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'nebulaemailscraper.middlewares.NebulaemailscraperDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "nebulaemailscraper.pipelines.EmailsDetailsPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 30
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
