from include.kaichan import kaichan
from urllib.parse import urlparse

def getConfig(url):
    parseURL = urlparse(url)
    domain = parseURL.netloc.replace('www.', '')

    if domain == "kaichan.co":
        return kaichan.CONFIGURATIONS.get(domain)
    else:
        return None