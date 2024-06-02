import argparse
import os

from function.main import *
from include.madara import madara
from include.mangareader import mangareader
from include.lolimanga import lolimanga
from include.mangasleep import mangasleep
from include.kaichan import kaichan
from include.manga00 import manga00
from include.toonsmanga import toonsmanga
from include.watashitachimanga import watashitachimanga

import checkURL

def arr():
    parser = argparse.ArgumentParser(description="Provide some Manga URL to start download images.")

    parser.add_argument('--murl', '-m', dest='murl', metavar='MURL', type=str, help="Enter Manga URL to process.")
    parser.add_argument('--start', '-s', dest='start', metavar='START', type=int, default=0, help="Specify chapter number to start download.")
    parser.add_argument('--end', '-e', dest='end', metavar='END', type=int, help="Specify chapter number to stop download.")
    parser.add_argument('--output', '-o', dest='output', metavar='OUTPUT', type=str, help="Enter output path to save downloaded.")
    parser.add_argument('--workthreads', '-wt', dest='workthreads', metavar='WORKTHREADS', type=int, help="Enter amount of threads to process.")
    parser.add_argument('--imagethreads', '-it', dest='imagethreads', metavar='IMAGETHREADS', type=int, help="Enter amount of threads to download image(s).")
    parser.add_argument('--wait', '-w', dest='wait', metavar='WAIT', type=int, help="Enter time to delay read page until loaded (In second).")
    parser.add_argument('--list', '-l', dest='list', action='store_true', help="Display Chapter list only")
    parser.add_argument('--debug', '-d', dest='debug', action='store_true', help="Enable debug mode for check bug(s) from any process.")
    parser.add_argument('--saveastext', '-sat', dest='saveastext', action='store_true', help="Save information as text.")
    parser.add_argument('--update', '-u', dest='update', action='store_true', help='Update from save information text files.')
    parser.add_argument('--verifyimg', '-vi', dest='verifyimg', action='store_true', help='Enable check the images downloaded and save as text files')
    args = parser.parse_args()

    if args.murl is not None:
        manga_url = args.murl

        if args.start is not None:
            start = int(args.start)
        else:
            start = None

        if args.end is not None:
            end = int(args.end)
        else:
            end = None
        
        if args.output is not None:
            output = args.output
        else:
            output = os.getcwd()

        if args.workthreads is not None:
            workthreads = int(args.workthreads)
        else:
            workthreads = 1

        if args.imagethreads is not None:
            imagethreads = int(args.imagethreads)
        else:
            imagethreads = 1
        
        if args.wait is not None:
            wait = int(args.wait)
        else:
            wait = 1
        
        if args.list is True:
            listchapter = True
        else:
            listchapter = False

        if args.debug is True:
            debug = True
        else:
            debug = False

        if args.saveastext is True:
            saveastext = True
        else:
            saveastext = False

        if args.update is True:
            update = True
        else:
            update = False

        if args.verifyimg is True:
            verifyimg = True
        else:
            verifyimg = False
        
        return manga_url, start, end, output, workthreads, imagethreads, wait, listchapter, debug
    else:
        exit(1)

if __name__ == '__main__':
    # Get value from user input
    manga_url, start, end, output, workthreads, imagethreads, wait, listchapter, debug = arr()
    print()
    print("[------ USER INPUT ------]")
    print(f"Manga URL: {manga_url}")
    print(f"Start: {start}")
    print(f"End: {end}")
    print(f"Output: {output}")
    print(f"Work Threads: {workthreads}")
    print(f"Image Threads: {imagethreads}")
    print(f"Delay: {wait}")
    print(f"List Chapters: {listchapter}")
    print(f"Debug Mode: {debug}")
    print()

    site = checkURL.checkURL(manga_url)

    if site == 'mangareader':
        mangareader.fetchmanga(manga_url, start, end, output, workthreads, imagethreads, wait, listchapter, debug)
    elif site == 'madara':
        madara.fetchmanga(manga_url, start, end, output, workthreads, imagethreads, wait, listchapter, debug)
    elif site == 'lolimanga':
        lolimanga.fetchmanga(manga_url, start, end, output, workthreads, imagethreads, wait, listchapter, debug)
    elif site =='mangasleep':
        mangasleep.fetchmanga(manga_url, start, end, output, workthreads, imagethreads, wait, listchapter, debug)
    elif site == 'kaichan':
        kaichan.fetchmanga(manga_url, start, end, output, workthreads, imagethreads, wait, listchapter, debug)
    elif site =='manga00':
        manga00.fetchmanga(manga_url, start, end, output, workthreads, imagethreads, wait, listchapter, debug)
    elif site == 'toonsmanga':
        toonsmanga.fetchmanga(manga_url, start, end, output, workthreads, imagethreads, wait, listchapter, debug)
    elif site =='watashitachimanga':
        watashitachimanga.fetchmanga(manga_url, start, end, output, workthreads, imagethreads, wait, listchapter, debug)
    else:
        print("URL not supported")
        exit()