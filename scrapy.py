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

import checkURL

def arr():
    parser = argparse.ArgumentParser(description="Provide some Manga URL to start download images.")

    parser.add_argument('--murl', '-m', dest='murl', metavar='MURL', type=str, help="Enter Manga URL to process.")
    parser.add_argument('--start', '-s', dest='start', metavar='START', type=int, default=0, help="Specify chapter number to start download.")
    parser.add_argument('--end', '-e', dest='end', metavar='END', type=int, help="Specify chapter number to stop download.")
    parser.add_argument('--output', '-o', dest='output', metavar='OUTPUT', type=str, help="Enter output path to save downloaded.")
    parser.add_argument('--threads', '-t', dest='threads', metavar='THREADS', type=int, help="Enter amount of threads to run.")
    parser.add_argument('--delay', '-d', dest='delay', metavar='DELAY', type=int, help="Enter time to delay read page until loaded (In second).")
    parser.add_argument('--list', '-l', dest='list', action='store_true', help="Display Chapter list only")

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

        if args.threads is not None:
            threads = int(args.threads)
        else:
            threads = 1
        
        if args.delay is not None:
            delay = int(args.delay)
        else:
            delay = 1
        
        if args.list is True:
            listchapter = True
        else:
            listchapter = False
        
        return manga_url, start, end, output, threads, delay, listchapter
    else:
        exit(1)

if __name__ == '__main__':
    # Get value from user input
    manga_url, start, end, output, threads, delay, listchapter = arr()
    print()
    print("[------ USER INPUT ------]")
    print(f"Manga URL: {manga_url}")
    print(f"Start: {start}")
    print(f"End: {end}")
    print(f"Output: {output}")
    print(f"Threads: {threads}")
    print(f"Delay: {delay}")
    print(f"List Chapters: {listchapter}")
    print()

    site = checkURL.checkURL(manga_url)

    if site == 'mangareader':
        mangareader.fetchmanga(manga_url, start, end, output, threads, delay, listchapter)
    elif site == 'madara':
        madara.fetchmanga(manga_url, start, end, output, threads, delay, listchapter)
    elif site == 'lolimanga':
        lolimanga.fetchmanga(manga_url, start, end, output, threads, delay, listchapter)
    elif site =='mangasleep':
        mangasleep.fetchmanga(manga_url, start, end, output, threads, delay, listchapter)
    elif site == 'kaichan':
        kaichan.fetchmanga(manga_url, start, end, output, threads, delay, listchapter)
    elif site =='manga00':
        manga00.fetchmanga(manga_url, start, end, output, threads, delay, listchapter)
    elif site == 'toonsmanga':
        toonsmanga.fetchmanga(manga_url, start, end, output, threads, delay, listchapter)
    else:
        print("URL not supported")
        exit()