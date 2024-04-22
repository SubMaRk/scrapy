from include.mangasleep import mangasleep
from urllib.parse import urlparse

def getConfig(url):
    parseURL = urlparse(url)
    domain = parseURL.netloc.replace('www.', '')

    if domain == "mangasleep.com":
        return mangasleep.CONFIGURATIONS.get(domain)
    else:
        return None