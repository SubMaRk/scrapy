from include.manga00 import manga00
from urllib.parse import urlparse

def getConfig(url):
    parseURL = urlparse(url)
    domain = parseURL.netloc.replace('www.', '')

    if domain == "manga00.com":
        return manga00.CONFIGURATIONS.get(domain)
    else:
        return None