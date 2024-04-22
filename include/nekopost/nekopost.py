from include.nekopost import config
from urllib.parse import urlparse

def getConfig(url):
    parseURL = urlparse(url)
    domain = parseURL.netloc.replace('www.', '')

    if domain == "nekopost.net":
        return config.CONFIGURATIONS.get(domain)
    else:
        return None