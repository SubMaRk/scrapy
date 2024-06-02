from urllib.parse import urlparse

# General
from include.madara.general import kapimanga
from include.madara.general import chocomanga
from include.madara.general import moritoon
from include.madara.general import mangalc
from include.madara.general import manhuathai
from include.madara.general import manhuabug
from include.madara.general import sixmanga
from include.madara.general import nabeemanga
from include.madara.general import kumotran
from include.madara.general import manhuakey
from include.madara.general import doodmanga
from include.madara.general import haremmanhua
from include.madara.general import mangapost
from include.madara.general import mangaisekaithai
from include.madara.general import catstranslator
from include.madara.general import manga191
from include.madara.general import mangasuper
from include.madara.general import rh2plusmanga

# Adult

def getConfig(url):
    parseURL = urlparse(url)
    domain = parseURL.netloc.replace('www.', '')

    if domain == "kapimanga.com":
        return kapimanga.CONFIGURATIONS.get(domain)
    elif domain == "chocomanga.com":
        return chocomanga.CONFIGURATIONS.get(domain)
    elif domain == "moritoon.com":
        return moritoon.CONFIGURATIONS.get(domain)
    elif domain == "manga-lc.net":
        return mangalc.CONFIGURATIONS.get(domain)
    elif domain == "manhuathai.com":
        return manhuathai.CONFIGURATIONS.get(domain)
    elif domain == "manhuabug.com":
        return manhuabug.CONFIGURATIONS.get(domain)
    elif domain == "sixmanga.com":
        return sixmanga.CONFIGURATIONS.get(domain)
    elif domain == "nabee-manga.com":
        return nabeemanga.CONFIGURATIONS.get(domain)
    elif domain == "kumotran.com":
        return kumotran.CONFIGURATIONS.get(domain)
    elif domain == "manhuakey.com":
        return manhuakey.CONFIGURATIONS.get(domain)
    elif domain == "doodmanga.com":
        return doodmanga.CONFIGURATIONS.get(domain)
    elif domain == "haremmanhua.com":
        return haremmanhua.CONFIGURATIONS.get(domain)
    elif domain == "manga-post.com":
        return mangapost.CONFIGURATIONS.get(domain)
    elif domain == "mangaisekaithai.com":
        return mangaisekaithai.CONFIGURATIONS.get(domain)
    elif domain == "cats-translator.com":
        return catstranslator.CONFIGURATIONS.get(domain)
    elif domain == "manga191.com":
        return manga191.CONFIGURATIONS.get(domain)
    elif domain == "mangasuper.com":
        return mangasuper.CONFIGURATIONS.get(domain)
    elif domain == "rh2plusmanga.com":
        return rh2plusmanga.CONFIGURATIONS.get(domain)
    else:
        return None