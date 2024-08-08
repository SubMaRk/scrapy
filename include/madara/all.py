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
from include.madara.general import catzaa
from include.madara.general import nanomanga
from include.madara.general import mangauptocats
from include.madara.general import manghaha
from include.madara.general import dokimori
from include.madara.general import kuromanga
from include.madara.general import manhwabreakup
from include.madara.general import thaitoon
from include.madara.general import zurushin

# Adult
from include.madara.adult import doujinfast
from include.madara.adult import doujinxh
from include.madara.adult import doujinlc
from include.madara.adult import kurodoujin
from include.madara.adult import doujinza
from include.madara.adult import superdoujin

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
        return mangasuper.CONFIGURATIONS.get(domain) # TODO: Wait for bypassing Cloudflare
    elif domain == "rh2plusmanga.com":
        return rh2plusmanga.CONFIGURATIONS.get(domain)
    elif domain == "catzaa.com":
        return catzaa.CONFIGURATIONS.get(domain)
    elif domain == "nano-manga.com":
        return nanomanga.CONFIGURATIONS.get(domain)
    elif domain == "manga-uptocats.com":
        return mangauptocats.CONFIGURATIONS.get(domain)
    elif domain == "manghaha.com":
        return manghaha.CONFIGURATIONS.get(domain) # TODO: Wait for support chapter list pages
    elif domain == "dokimori.com":
        return dokimori.CONFIGURATIONS.get(domain)
    elif domain == "kuro-manga.com":
        return kuromanga.CONFIGURATIONS.get(domain)
    elif domain == "manhwabreakup.com":
        return manhwabreakup.CONFIGURATIONS.get(domain)
    elif domain == "thaitoon.net":
        return thaitoon.CONFIGURATIONS.get(domain)
    elif domain == "zurushin.com":
        return zurushin.CONFIGURATIONS.get(domain)
    elif domain == "doujinfast.com":
        return doujinfast.CONFIGURATIONS.get(domain)
    elif domain == "doujinx-h.com":
        return doujinxh.CONFIGURATIONS.get(domain)
    elif domain == "doujin-lc.net":
        return doujinlc.CONFIGURATIONS.get(domain) # TODO: Wait for bypassing Cloudflare
    elif domain == "kuro-doujin.com":
        return kurodoujin.CONFIGURATIONS.get(domain)
    elif domain == "doujinza.com":
        return doujinza.CONFIGURATIONS.get(domain)
    elif domain == "superdoujin.org":
        return superdoujin.CONFIGURATIONS.get(domain)
    else:
        return None
    