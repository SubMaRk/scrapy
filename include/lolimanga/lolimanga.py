from include.lolimanga import lolimanga
from urllib.parse import urlparse

def getConfig(url):
    parseURL = urlparse(url)
    domain = parseURL.netloc.replace('www.', '')

    if domain == "loli-manga.com":
        return lolimanga.CONFIGURATIONS.get(domain)
    else:
        return None