from function.main import *
from include.madara import madara
from include.mangareader import mangareader
from include.lolimanga import lolimanga
from include.mangasleep import mangasleep
from include.kaichan import kaichan
from include.manga00 import manga00
from include.toonsmanga import toonsmanga

import checkURL

if __name__ == '__main__':
    #arr()

    url = input("Enter a URL to download: ")

    site = checkURL.checkURL(url)

    if site == 'mangareader':
        mangareader.fetchmanga(url)
    elif site == 'madara':
        madara.fetchmanga(url)
    elif site == 'lolimanga':
        lolimanga.fetchmanga(url)
    elif site =='mangasleep':
        mangasleep.fetchmanga(url)
    elif site == 'kaichan':
        kaichan.fetchmanga(url)
    elif site =='manga00':
        manga00.fetchmanga(url)
    elif site == 'toonsmanga':
        toonsmanga.fetchmanga(url)
    else:
        print("URL not supported")
        exit()