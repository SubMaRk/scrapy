from urllib.parse import urlparse

def checkURL(url):
    parseURL = urlparse(url)
    domain = parseURL.netloc.replace('www.', '')
    mangareader_site = ['thaimanga.net',
        'manga689.com',
        'manga168.com',
        'tamamanga.com',
        'xn--l3c0azab5a2gta.com',
        'ped-manga.com',
        'sing-manga.com',
        'mangakimi.com',
        'me-manga.com',
        'reapertrans.com',
        'dragon-manga.com',
        'moodtoon.com',
        'toomtam-manga.com',
        'miku-manga.com',
        'asurahunter.com',
        '108-manga.com',
        'joji-manga.com',
        'spy-manga.com',
        'murim-manga.com',
        'mangastep.com',
        'jaymanga.com',
        'hippomanga.com',
        'popsmanga.com',
        'tanuki-manga.com',
        'inu-manga.com',
        'lami-manga.com',
        'weimanga.com',
        'slow-manga.com',
        'makimaaaaa.com',
        'kazetori-manga.com',
        'kumomanga.net',
        'flash-manga.com',
        'manga-za.net',
        'oremanga.net',
        'manhwathailand.com',
        'romance-manga.com',
        'germa-66.com',
        'xn--72ca2cvbi6fe9m.com',
        'go-manga.com',
        'up-manga.com',
        'god-manga.com',
        'rose-manga.com',
        'xn--72cas2cj6a4hf4b5a8oc.com',
        'seetoon.net',
        'skoiiz-manga.com',
        'manga-sugoi.com',
        'manga-i.com',
        'ranker-manga.com',
        'manga248.com',
        'haremmanga.net',
        'webtoonmanga.com',
        'manhwathaiplus.net',
        'funtoons.online',
        'mafia-manga.com',
        'xenon-manga.com',
        'mangalami.com',
        'mangawei.com',
        'manhwa-thailand.com',
        'one-manga.com',
        'thetoon101.com',# Doujin Sites
        'god-doujin.com',
        'doujin69.com',
        'doujin-new.com',
        'oredoujin.com',
        'doujin-y.com',
        'toonhunter.com',
        'doujinmoon.com',
        'ecchi-doujin.com',
        'doujin4u.com',
        'xn--69-uqi5m9an.com',
        '108read.com',
        'ped-doujin.com',
        'eye-manga.com',
        'manga-20.com',
        'manga-yuri.com',
        'tora-manga.com',
        'manga-bl.com',
        'manga-yaoi.com',
        'xn--72ca0fgy7cem.com',
        'ntr-manga.com',
        '18ntr.com',
        'godhman.net'
        ]
    
    madara_site = ['nabee-manga.com',
        'manga-post.com',
        'sixmanga.com',
        'snap-manga.com',
        'manga-lc.net',
        'mangaisekaithai.com',
        'cats-translator.com',
        'manga191.com',
        'rh2plusmanga.com',
        'mangasuper.com',
        'doodmanga.com',
        'catzaa.com',
        'moritoon.com',
        'nano-manga.com',
        'manga-uptocats.com',
        'haremmanhua.com',
        'manghaha.com',
        'dokimori.com',
        'kuro-manga.com',
        'manhwabreakup.com',
        'manhuabug.com',
        'thaitoon.net',
        'zurushin.com',
        'manhuathai.com',
        'chocomanga.com',
        'wasabith.com',
        'kapimanga.com',
        'kumotran.com',
        'manhuakey.com',# Doujin Sites
        'doujinfast.com',
        'doujinx-h.com',
        'doujinza.com',
        'kuro-doujin.com',
        'doujin-lc.net',
        'doujinsuki.com',
        'superdoujin.org',
        'yaoi-y.com',
        'ok-doujinx.com',]
    
    lolimanga = 'loli-manga.com'
    mangasleep = 'mangasleep.com'
    kaichan = 'kaichan.co'
    manga00 = 'manga00.com'
    toonsmanga = 'toonsmanga.com'
    watashitachimanga = 'watashitachimanga.com'

    if domain in mangareader_site:
        return 'mangareader'
    elif domain in madara_site:
        return 'madara'
    elif domain == lolimanga:
        return 'lolimanga'
    elif domain == mangasleep:
        return 'mangasleep'
    elif domain == kaichan:
        return 'kaichan'
    elif domain == manga00:
        return 'manga00'
    elif domain == toonsmanga:
        return 'toonsmanga'
    elif domain == watashitachimanga:
        return 'watashitachimanga'
    else:
        return False