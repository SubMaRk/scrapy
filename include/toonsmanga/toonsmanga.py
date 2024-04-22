from include.toonsmanga import toonsmanga
from urllib.parse import urlparse

def getConfig(url):
    parseURL = urlparse(url)
    domain = parseURL.netloc.replace('www.', '')

    if domain == "toonsmanga.com":
        return toonsmanga.CONFIGURATIONS.get(domain)
    else:
        return None