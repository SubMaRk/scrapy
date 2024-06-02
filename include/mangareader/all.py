from urllib.parse import urlparse

# General
from include.mangareader.general import oremanga
from include.mangareader.general import manga168
from include.mangareader.general import thaimanga
from include.mangareader.general import singmanga
from include.mangareader.general import manga689
from include.mangareader.general import dragonmanga
from include.mangareader.general import mangakimi
from include.mangareader.general import mangastep
from include.mangareader.general import reapertrans
from include.mangareader.general import tanukimanga
from include.mangareader.general import spymanga
from include.mangareader.general import mafiamanga
from include.mangareader.general import xenonmanga
from include.mangareader.general import manga108
from include.mangareader.general import asurahunter
from include.mangareader.general import flashmanga
from include.mangareader.general import sodsaime
from include.mangareader.general import murimmanga
from include.mangareader.general import moodtoon
from include.mangareader.general import pedmanga
from include.mangareader.general import toomtammanga
from include.mangareader.general import mikumanga
from include.mangareader.general import jojimanga
from include.mangareader.general import kumomanga
from include.mangareader.general import hippomanga
from include.mangareader.general import inumanga
from include.mangareader.general import makimaaaaa
from include.mangareader.general import slowmanga
from include.mangareader.general import mangawei
from include.mangareader.general import kazetorimanga
from include.mangareader.general import godmanga
from include.mangareader.general import upmanga
from include.mangareader.general import gomanga
from include.mangareader.general import mangathai
from include.mangareader.general import skoiizmanga
from include.mangareader.general import germa66
from include.mangareader.general import romancemanga
from include.mangareader.general import manhwathailand
from include.mangareader.general import mangaza
from include.mangareader.general import rosemanga
from include.mangareader.general import mangayipun
from include.mangareader.general import seetoon
from include.mangareader.general import mangasugoi
from include.mangareader.general import mangai
from include.mangareader.general import rankermanga
from include.mangareader.general import manga248
from include.mangareader.general import manhwathaiplus
from include.mangareader.general import thetoon101
from include.mangareader.general import onemanga
from include.mangareader.general import popmanga
from include.mangareader.general import mangalami
from include.mangareader.general import haremmanga

# Adult
from include.mangareader.adult import toonhunter
from include.mangareader.adult import ntrmanga
from include.mangareader.adult import goddoujin
from include.mangareader.adult import doujin69
from include.mangareader.adult import doujinnew
from include.mangareader.adult import oredoujin
from include.mangareader.adult import eike69
from include.mangareader.adult import doujin4u
from include.mangareader.adult import godhman
from include.mangareader.adult import ecchidoujin
from include.mangareader.adult import doujiny
from include.mangareader.adult import doujinmoon
from include.mangareader.adult import read108
from include.mangareader.adult import peddoujin
from include.mangareader.adult import eyemanga
from include.mangareader.adult import toramanga
from include.mangareader.adult import mangayuri
from include.mangareader.adult import manga20
from include.mangareader.adult import mangabl
from include.mangareader.adult import mangayaoi
from include.mangareader.adult import mangay
from include.mangareader.adult import ntr18

def getConfig(url):
    parseURL = urlparse(url)
    domain = parseURL.netloc.replace('www.', '')

    if domain == "oremanga.net":
        return oremanga.CONFIGURATIONS.get(domain)
    elif domain == "manga168.com":
        return manga168.CONFIGURATIONS.get(domain)
    elif domain == "thaimanga.net":
        return thaimanga.CONFIGURATIONS.get(domain)
    elif domain == "sing-manga.com":
        return singmanga.CONFIGURATIONS.get(domain)
    elif domain == "manga689.com":
        return manga689.CONFIGURATIONS.get(domain)
    elif domain == "toonhunter.com":
        return toonhunter.CONFIGURATIONS.get(domain)
    elif domain == "dragon-manga.com":
        return dragonmanga.CONFIGURATIONS.get(domain)
    elif domain == "mangakimi.com":
        return mangakimi.CONFIGURATIONS.get(domain)
    elif domain == "mangastep.com":
        return mangastep.CONFIGURATIONS.get(domain)
    elif domain == "reapertrans.com":
        return reapertrans.CONFIGURATIONS.get(domain)
    elif domain == "tanuki-manga.com":
        return tanukimanga.CONFIGURATIONS.get(domain)
    elif domain == "spy-manga.com":
        return spymanga.CONFIGURATIONS.get(domain)
    elif domain == "mafia-manga.com":
        return mafiamanga.CONFIGURATIONS.get(domain)
    elif domain == "ntr-manga.com":
        return ntrmanga.CONFIGURATIONS.get(domain)
    elif domain == "xenon-manga.com":
        return xenonmanga.CONFIGURATIONS.get(domain)
    elif domain == "108-manga.com":
        return manga108.CONFIGURATIONS.get(domain)
    elif domain == "asurahunter.com":
        return asurahunter.CONFIGURATIONS.get(domain)
    elif domain == "flash-manga.com":
        return flashmanga.CONFIGURATIONS.get(domain)
    elif domain == "xn--l3c0azab5a2gta.com":
        return sodsaime.CONFIGURATIONS.get(domain)
    elif domain == "murim-manga.com":
        return murimmanga.CONFIGURATIONS.get(domain)
    elif domain == "moodtoon.com":
        return moodtoon.CONFIGURATIONS.get(domain)
    elif domain == "ped-manga.com":
        return pedmanga.CONFIGURATIONS.get(domain)
    elif domain == "toomtam-manga.com":
        return toomtammanga.CONFIGURATIONS.get(domain)
    elif domain == "miku-manga.com":
        return mikumanga.CONFIGURATIONS.get(domain)
    elif domain == "joji-manga.com":
        return jojimanga.CONFIGURATIONS.get(domain)
    elif domain == "kumomanga.net":
        return kumomanga.CONFIGURATIONS.get(domain)
    elif domain == "hippomanga.com":
        return hippomanga.CONFIGURATIONS.get(domain)
    elif domain == "inu-manga.com":
        return inumanga.CONFIGURATIONS.get(domain)
    elif domain == "makimaaaaa.com":
        return makimaaaaa.CONFIGURATIONS.get(domain)
    elif domain == "slow-manga.com":
        return slowmanga.CONFIGURATIONS.get(domain)
    elif domain == "mangawei.com":
        return mangawei.CONFIGURATIONS.get(domain)
    elif domain == "kazetori-manga.com":
        return kazetorimanga.CONFIGURATIONS.get(domain)
    elif domain == "god-manga.com":
        return godmanga.CONFIGURATIONS.get(domain)
    elif domain == "up-manga.com":
        return upmanga.CONFIGURATIONS.get(domain)
    elif domain == "go-manga.com":
        return gomanga.CONFIGURATIONS.get(domain)
    elif domain == "xn--72ca2cvbi6fe9m.com":
        return mangathai.CONFIGURATIONS.get(domain)
    elif domain == "skoiiz-manga.com":
        return skoiizmanga.CONFIGURATIONS.get(domain)
    elif domain == "germa-66.com":
        return germa66.CONFIGURATIONS.get(domain)
    elif domain == "romance-manga.com":
        return romancemanga.CONFIGURATIONS.get(domain)
    elif domain == "manhwa-thailand.com":
        return manhwathailand.CONFIGURATIONS.get(domain)
    elif domain == "manhwathaiplus.net":
        return manhwathaiplus.CONFIGURATIONS.get(domain)
    elif domain == "manga-za.net":
        return mangaza.CONFIGURATIONS.get(domain)
    elif domain == "rose-manga.com":
        return rosemanga.CONFIGURATIONS.get(domain)
    elif domain == "xn--72cas2cj6a4hf4b5a8oc.com":
        return mangayipun.CONFIGURATIONS.get(domain)
    elif domain == "seetoon.net":
        return seetoon.CONFIGURATIONS.get(domain)
    elif domain == "manga-sugoi.com":
        return mangasugoi.CONFIGURATIONS.get(domain)
    elif domain == "manga-i.com":
        return mangai.CONFIGURATIONS.get(domain)
    elif domain == "ranker-manga.com":
        return rankermanga.CONFIGURATIONS.get(domain)
    elif domain == "manga248.com":
        return manga248.CONFIGURATIONS.get(domain)
    elif domain == "thetoon101.com":
        return thetoon101.CONFIGURATIONS.get(domain)
    elif domain == "one-manga.com":
        return onemanga.CONFIGURATIONS.get(domain)
    elif domain == "popsmanga.com":
        return popmanga.CONFIGURATIONS.get(domain)
    elif domain == "mangalami.com":
        return mangalami.CONFIGURATIONS.get(domain)
    elif domain == "haremmanga.net":
        return haremmanga.CONFIGURATIONS.get(domain)
    elif domain == "god-doujin.com":
        return goddoujin.CONFIGURATIONS.get(domain)
    elif domain == "doujin69.com":
        return doujin69.CONFIGURATIONS.get(domain)
    elif domain == "doujin-new.com":
        return doujinnew.CONFIGURATIONS.get(domain)
    elif domain == "oredoujin.com":
        return oredoujin.CONFIGURATIONS.get(domain)
    elif domain == "xn--69-uqi5m9an.com":
        return eike69.CONFIGURATIONS.get(domain)
    elif domain == "doujin4u.com":
        return doujin4u.CONFIGURATIONS.get(domain)
    elif domain == "godhman.net":
        return godhman.CONFIGURATIONS.get(domain)
    elif domain == "ecchi-doujin.com":
        return ecchidoujin.CONFIGURATIONS.get(domain)
    elif domain == "doujin-y.com":
        return doujiny.CONFIGURATIONS.get(domain)
    elif domain == "doujinmoon.com":
        return doujinmoon.CONFIGURATIONS.get(domain)
    elif domain == "108read.com":
        return read108.CONFIGURATIONS.get(domain)
    elif domain == "ped-doujin.com":
        return peddoujin.CONFIGURATIONS.get(domain)
    elif domain == "eye-manga.com":
        return eyemanga.CONFIGURATIONS.get(domain)
    elif domain == "tora-manga.com":
        return toramanga.CONFIGURATIONS.get(domain)
    elif domain == "manga-yuri.com":
        return mangayuri.CONFIGURATIONS.get(domain)
    elif domain == "manga-20.com":
        return manga20.CONFIGURATIONS.get(domain)
    elif domain == "manga-bl.com":
        return mangabl.CONFIGURATIONS.get(domain)
    elif domain == "manga-yaoi.com":
        return mangayaoi.CONFIGURATIONS.get(domain)
    elif domain == "xn--72ca0fgy7cem.com":
        return mangay.CONFIGURATIONS.get(domain)
    elif domain == "18ntr.com":
        return ntr18.CONFIGURATIONS.get(domain)
    else:
        return None