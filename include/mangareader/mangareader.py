import latest_user_agents
import requests as rq
from bs4 import BeautifulSoup as bs
import time
import datetime
from function import main
from urllib.parse import urlparse
import urllib.parse
import re
import os
import random
import json
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from include.mangareader import all

def get_user_agent():
    # Get all the latest user agents
    all_user_agents = latest_user_agents.get_latest_user_agents()

    # Filter the list to get only the Chrome user agent
    chrome_user_agent = next(user_agent for user_agent in all_user_agents if 'Chrome/' and 'NT' and 'Win64' in user_agent)

    return chrome_user_agent

def getHeaders():
    user_agent = get_user_agent()
    headers = {
        'User-Agent': user_agent,
        'Accept-Language': 'th-TH,th;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    return headers

def bssoup(url):
    # Set headers
    headers = getHeaders()
    max_retires = 6
    delay = 10
    for retry in range(max_retires):
        try:
            response = rq.get(url, headers=headers)
            response.raise_for_status()
        except rq.exceptions.RequestException as e:
            # Handle request-related errors
            print(f"Retry {retry + 1}: Failed to fetch the page. HTTP status code: {response.status_code}")
            time.sleep(delay)
        except rq.exceptions.HTTPError as e:
            # Handle request-related errors
            print(f"Retry {retry + 1}: Failed to fetch the page. HTTP status code: {response.status_code}")
            time.sleep(delay)
        except Exception as e:
            # Handle other unexpected exceptions
            print(f"Retry {retry + 1}: Failed to fetch the page. HTTP status code: {response.status_code}")
            time.sleep(delay)
        else:
            soup = bs(response.content, "html.parser")
            break
    return soup

def gettime():
    return time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())

def findChapters(section, div):
    print(f"Finding chapters from {div}...")

    try:
        chapters = section.select(div)
        if chapters:
            return chapters
        else:
            raise ValueError(f"Status {div} not found.")
    except Exception as e:
        print(f"Error finding status {div}: {e}")
        return None
    
def findCover(section, div):
    print(f"Finding cover from {div}...")

    try:
        cover = section.select(div)
        if cover:
            return cover
        else:
            raise ValueError(f"Status {div} not found.")
    except Exception as e:
        print(f"Error finding status {div}: {e}")
        return None

def fetchmanga(url, start, end, output, workthreads, imagethreads, wait, listchapter, debug, savejson, update):
    global readdiv, readjson, readencrypt
    output = os.path.join(output, "Download")
    logfolder = "log"
    main.mkdir(logfolder)
    logfile = os.path.join(logfolder, "error.log")
    notablefile = os.path.join(logfolder, "nochapter.log")
    successfile = os.path.join(logfolder, "finished.log")
    mangaID = main.manga_id(url)

    main.mkdir(output)

    # get the config for the domain
    print(f"Getting configuration for {url}...")
    config = all.getConfig(url)
    if config is None:
        if debug is True:
            print("Error! Missing the configuration file to process this URL.")
        return None
    else:
        print()
        print(f"[------ Found configuration ------]")
        # Use config variables
        getsection = config["getsection"]
        gettitle = config["gettitle"]
        gettype = config["gettype"]
        getgenre = config["getgenre"]
        getstatus = config["getstatus"]
        getchapterlist = config["getchapterlist"]
        getcover = config["getcover"]
        getchaptertitle = config["getchaptertitle"]
        readdiv = config["readdiv"]
        delaylist = config["delaylist"]
        readjson = config["readjson"]
        readencrypt = config["readencrypt"]

        print(f"Section: {getsection}")
        print(f"Title: {gettitle}")
        print(f"Type: {gettype}")
        print(f"Genre: {getgenre}")
        print(f"Status: {getstatus}")
        print(f"Chapter List: {getchapterlist}")
        print(f"Cover: {getcover}")
        print(f"Chapter Title: {getchaptertitle}")
        print(f"Read Div: {readdiv}")
        print(f"Delay List: {delaylist}")
        print(f"Read JSON: {readjson}")
        print(f"Read Encrypt: {readencrypt}")
        print()
        if debug is True:
            print("\nVerify to ensure that the configuration file is correct.")
            main.waitforact()

    # Find Section
    print(f"Fetching manga information...")
    soup = bssoup(url)
    
    try:
        section = soup.select_one(getsection)
        #print(section)
    except Exception as e:
        print(f"Error finding section {getsection}: {e}")
        currenttime = gettime()
        main.write_file(logfile, f"{currenttime}: Failed to find manga information from {url}\n")
        return None
    
    # Fetch manga information
    print()
    print('[------ MANGA INFORMATION ------]')

    # Title
    try:
        title = section.select_one(gettitle).getText()
        mgTitle = re.sub(r'[\\/:"*?<>|]', '', title)
    except Exception as e:
        print(f"Error finding title from {gettitle}: {e}")
        currenttime = gettime()
        main.write_file(logfile, f"{currenttime}: Failed to find manga title from {url}\n")
        return None
    print(f"Title: {mgTitle}")
    if debug is True:
        main.waitforact()
    
    # Type
    mgtype = None
    try:
        type = section.select_one(gettype)
        mgtype = type.get_text()
    except Exception as e:
        pass

    if not mgtype:
        try:
            type = section.find_all("div", class_=f"{gettype}")
            type = type[1].find('a')
            mgtype = type.text.strip()
        except Exception as e:
            pass

    if not mgtype:
        try:
            type = section.find("td", string=f"{gettype}")
            type = type.find_next_sibling('td')
            mgtype = type.text.strip()
        except Exception as e:
            print(f"Error finding type from {gettype}: {e}")
            mgtype = ''
    print(f"Type: {mgtype}")
    if debug is True:
        main.waitforact()

    # Genres
    mggenres = []
    try:
        genres = section.select_one(getgenre).find_all('a')
        for genre in genres:
            genre = genre.get_text()
            mggenres.append(genre)
        mggenres = ", ".join(mggenres)
    except Exception as e:
        print(f"Error finding genres from {getgenre}: {e}")
        mggenres = ''
    print(f"Genres: {mggenres}")
    if debug is True:
        main.waitforact()
    
    # Status
    mgstatus = None
    try:
        status = section.select_one(getstatus)
        mgstatus = status.get_text()
    except Exception as e:
        pass

    if not mgstatus:
        try:
            status = section.find_all("div", class_=f"{getstatus}")
            status = status[0].find('i')
            mgstatus = status.text.strip()
        except Exception as e:
            pass

    if not mgstatus:
        try:
            status = section.find("td", string=f"{getstatus}")
            status = status.find_next_sibling('td')
            mgstatus = status.text.strip()
        except Exception as e:
            print(f"Error finding status from {getstatus}: {e}")
            mgstatus = ''
    print(f"Status: {mgstatus}")
    if debug is True:
        main.waitforact()

    # Chapters
    try:
        chapters = section.select_one(getchapterlist)
        chapterslist = chapters.find_all('li')
        beforecount = len(chapterslist)
    except Exception as e:
        print(f"Error finding chapter from {getchapterlist}: {e}")
        chapterslist = ''

    titlelinks = []
    if chapterslist:
        data_num = ''
        first_chapter = chapterslist[0]
        data_num = main.extract_num(first_chapter, mgTitle, url)

        if data_num > 1 and beforecount > 1:
            chapterslist = list(reversed(chapterslist))
        
        first_chapter = chapterslist[0]
        data_num = main.extract_num(first_chapter, mgTitle, url)

        if start is not None and end is not None:
            start = int(start)
            end = int(end)
            if len(chapterslist) > start:
                if data_num == 0:
                    start = int(start) + 1
                else:
                    start = int(start)

                end = int(end) - start
            
                chapterslist = chapterslist[start:]
                chapterslist = chapterslist[:end]
            else:
                return None
        elif start is not None and end is None:
            start = int(start)
            if len(chapterslist) > start:
                if data_num == 0:
                    start = int(start) + 1
                else:
                    start = int(start)
                chapterslist = chapterslist[start:]
            else:
                return None
        elif start is None and end is not None:
            end = int(end)
            if len(chapterslist) <= end:
                chapterslist = chapterslist[:end]
            else:
                return None
        else:
            chapterslist = chapterslist

        first_chapter = chapterslist[0]
        last_chapter = chapterslist[-1]
        getfirstlink = first_chapter.find('a')['href']
        getlastlink = last_chapter.find('a')['href']
        first_chapter_url = urllib.parse.unquote(getfirstlink)
        last_chapter_url = urllib.parse.unquote(getlastlink)

        # Store the chapters url list;
        chapterslink = []
    
        for i, chapter in enumerate(chapterslist):
            cpurl = chapter.find('a')['href']
            if not cpurl.startswith('https'):
                break
            try:
                title = chapter.find('a')['title']
            except:
                title = chapter.find('a').find('span')
                title = title.get_text() if title else None

            parseurl = urllib.parse.unquote(cpurl)
            titlelinks.append([i+1, title, parseurl])
            if listchapter is True:
                print(f"{i+1} | {title} : {parseurl}")
            else:
                pass
            chapterslink.append(parseurl)
        else:
            if listchapter is True:
                return None
            else:
                pass
        
        aftercount = len(chapterslink)
    else:
        currenttime = gettime()
        main.write_file(logfile, f"{currenttime}: Failed to find chapter table from {url}\n")
        main.write_file(notablefile, f"{url}\n")
        return None
    print(f"Chapters: {aftercount}")
    if debug is True:
        main.waitforact()

    # Cover
    try:
        cover = section.select_one(getcover)
        mgCover = cover['data-src'] if 'data-src' in cover.attrs else cover['src'] if 'src' in cover.attrs else None
        if mgCover:
            if not mgCover.startswith('https:') and mgCover.startswith('//'):
                mgCover = 'https:' + mgCover
            cleanup = mgCover.rfind('?')
            if cleanup != -1:
                mgCover = mgCover[:cleanup]
    except Exception as e:
        print(f"Error finding cover from {getcover}: {e}")
        mgCover = ''
    print(f"Cover: {mgCover}")
    print()
    if debug is True:
        main.waitforact()
    
    folderName = os.path.join(output, mgTitle)
    main.mkdir(folderName)

    # Download cover image
    if mgCover:
        file_extension = os.path.splitext(mgCover)[1]
        cover_name = f"{mgTitle}{file_extension}"
        cover_path = os.path.join(folderName, cover_name)
        if os.path.exists(cover_path):
            print(f"Image {cover_name} already exists. Trying to check file integrity...")
            compare_result = main.compare_size(mgCover, cover_path, cover_name, logfile)
            if compare_result is False:
                currentTime = gettime()
                main.write_file(logfile, f"{currentTime}: The size of image {mgCover} from {url} not compared.\n")
        else:
            dl_result = main.dl_img(mgCover, cover_path, cover_name, logfile)
            if dl_result is False:
                print(f"Error to downloading {url}.")
                currentTime = gettime()
                main.write_file(logfile, f"{currentTime}: Failed to download the image {mgCover} from {url}.\n")
                return None
            else:
                print(f'{mgCover} => {cover_name}')
                compare_result = main.compare_size(mgCover, cover_path, cover_name, logfile)
                if compare_result is False:
                    currentTime = gettime()
                    main.write_file(logfile, f"{currentTime}: The size of image {mgCover} from {url} not compared.\n")

    if debug is True:
        main.waitforact()

    # Save data to json file
    if savejson is True:
        datafolder = "Data"
        main.mkdir(datafolder)
        parseURL = urlparse(url)
        domain = parseURL.netloc.replace('www.', '')
        dname = domain.split('.')[0]
        dpath = os.path.join(datafolder, dname)
        if not os.path.exists(dpath):
            main.mkdir(dpath)

        jsonfile = os.path.join(dpath, f"{mgTitle}.json")
        if not os.path.exists(jsonfile):
            main.savejson(jsonfile, mgTitle=mgTitle, mgtype=mgtype, mggenres=mggenres, mgstatus=mgstatus, chaptercount=aftercount)
            for i, data in enumerate(titlelinks):
                index, cptitle, cplink = data
                main.savejson(jsonfile, chaptertitle=cptitle, chapterurl=cplink)
        else:
            main.savejson(jsonfile, mgTitle=mgTitle, mgtype=mgtype, mggenres=mggenres, mgstatus=mgstatus, chaptercount=aftercount)
            mgtitle, mgtype, mggenres, mgStatus, chaptercount, chapterurls = main.readjson(jsonfile)
        if update is True:
            main.savejson(jsonfile, mgTitle=mgTitle, mgtype=mgtype, mggenres=mggenres, mgstatus=mgstatus)

        if debug is True:
            main.waitforact()
    
    skipdomains = ['googleusercontent.com',
        'https://img.toon88.com',
        'https://a3.manga168.xyz',
        'https://manga-online.co',
        'https://img.jeawnoi.com',
        'https://cmd.weimanga.com',
        'https://doujin2u.com',
        'humnoi.xyz',
        'https://dev.flash-manga.com',
        'https://p.doujin2u.com',
        'https://www.manga-online.co',
        'https://sgp1.vultrobjects.com',
        'https://al6.ped-manga.com',
        'https://dev.slow-manga.com',
        'blogspot.com',
        'https://media.niceoppai.net',
        'thload.com',
        'picz.in.th'
    ]

    # Start process chapters with multi-threaded
    workers = workthreads
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = []

        # Start fetching images from the chapter list;
        for i, chapter_url in enumerate(chapterslink):
            if savejson is True:
                if chapterurls is not None:
                    if chapter_url in chapterurls:
                        print(f"URL '{chapter_url}' already exists. Skipping addition.")
                        continue
                    else:
                        print(f"Start processing {chapter_url}...")
                        future = executor.submit(preparedl, i, chapter_url, url, mgTitle, getchaptertitle, mangaID, folderName, skipdomains, imagethreads, wait, logfile, debug, savejson, successfile, jsonfile)
                        futures.append(future)
                else:
                    print(f"Start processing {chapter_url}...")
                    future = executor.submit(preparedl, i, chapter_url, url, mgTitle, getchaptertitle, mangaID, folderName, skipdomains, imagethreads, wait, logfile, debug, savejson, successfile, jsonfile)
                    futures.append(future)
            else:
                print(f"Start processing {chapter_url}...")
                future = executor.submit(preparedl, i, chapter_url, url, mgTitle, getchaptertitle, mangaID, folderName, skipdomains, imagethreads, wait, logfile, debug, successfile, savejson)
                futures.append(future)

def preparedl(i, chapterURL, url, mgTitle, getchaptertitle, mangaID, folderName, skipdomains, imagethreads, wait, logfile, debug, savejson, successfile, jsonfile=None):
    soup = bssoup(chapterURL)

    # Find chapter title
    try:
        chapterTitle = soup.select_one(getchaptertitle).getText()
        titlename = re.sub(r'[\\/:"*?<>|]', '', chapterTitle)
        chapter = main.getchapter(mgTitle, titlename)
    except Exception as e:
        pass
    
    if not chapter:
        try:
            # Parse the URL
            decode_url = urllib.parse.urlparse(chapterURL)
            # Split the path
            path_parts = decode_url.path.split("/")
            # Extract the last part (which should be the chapter number)
            chapter = urllib.parse.unquote(path_parts[3])
            if not chapter:
                chapter = i
        except Exception as e:
            print(f"Error: {e}")
            currentTime = gettime()
            main.write_file(logfile, f"{currentTime}: Failed to find chapter number from {chapterURL}\n")
            return None
    
    chapterFoldername = f"Chapter-{chapter}"
    chapterPath = os.path.join(folderName, chapterFoldername)
    main.mkdir(chapterPath)
    
    getimg = findIMG(soup, chapterURL, readdiv, readjson, readencrypt, chapter, chapterPath, wait, logfile, debug)
    if getimg is True:
        print("Capture image from page successfully.")
        success = []
        if os.path.exists(successfile):
            success = main.read_file(successfile)
            if not url in success:
                success = f"{url}\n"
                main.write_file(successfile, success)
                print("Added chapter URL to success file.")
        else:
            main.write_file(successfile, f"{url}\n")
        if savejson is True:
            main.savejson(jsonfile, chaptertitle=chapterFoldername, chapterurl=chapterURL)
    elif getimg is None:
        return None
    else:
        count = main.countFiles(chapterPath)
        if count == len(getimg):
            success = []
            if os.path.exists(successfile):
                success = main.read_file(successfile)
                if not url in success:
                    success = f"{url}\n"
                    main.write_file(successfile, success)
                    print("Added chapter URL to success file.")
            else:
                main.write_file(successfile, f"{url}\n")
            if savejson is True:
                main.savejson(jsonfile, chaptertitle=chapterFoldername, chapterurl=chapterURL)
            return None
        
        workers = imagethreads
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            futures = []

            # Start fetching images from the chapter list;
            for i, img in enumerate(getimg):
                print(f"Start Downloading {img}...")
                future = executor.submit(downloadImg, i, img, url, chapterURL, chapter, chapterPath, skipdomains, logfile)
                futures.append(future)

        # Check downloaded files
        downloadedFiles = main.countFiles(chapterPath)
        if len(getimg) != downloadedFiles:
            print(f"Downloaded files: {downloadedFiles}")
            print(f"Expected files: {len(getimg)}")
            currentTime = gettime()
            main.write_file(logfile, f"{currentTime}: The number of downloaded files {downloadedFiles} from {chapterURL} not equal to expected files {len(getimg)}.\n")
            return None
        else:
            success = []
            if os.path.exists(successfile):
                success = main.read_file(successfile)
                if not url in success:
                    success = f"{url}\n"
                    main.write_file(successfile, success)
                    print("Added chapter URL to success file.")
            else:
                main.write_file(successfile, f"{url}\n")
            if savejson is True:
                main.savejson(jsonfile, chaptertitle=chapterFoldername, chapterurl=chapterURL)

def downloadImg(i, img, url, chapterURL, chapter, chapterPath, skipdomains, logfile):
    if not img.startswith('https:') and img.startswith('//'):
        img = 'https:' + img
    # Remove invalid characters from link;
    if "%0A" in img:
        img = img.replace("%0A", "")
    # Remove invalid url from link;
    if "https://doujin4u.com/wp-content/uploads/;" in img:
        img = img.replace("https://doujin4u.com/wp-content/uploads/;", "")

    # Check extension;
    file_extension = os.path.splitext(img)[1]
    if file_extension == ".webppng":
        img = img.replace(".webppng", ".webp")

    if not file_extension:
        print(f"Image link {img} has no extension. Skipping...")
        currentTime = gettime()
        main.write_file(logfile, f"{currentTime}: The image not have extenstion from {chapterURL}\n")
        return None
            
    if any(skip_domain in img for skip_domain in skipdomains):
        print(f"Image link {img} has skip domain. Skipping...")
        currentTime = gettime()
        main.write_file(logfile, f"{currentTime}: The image found in skip domain from {chapterURL}\n")
        return None
            
    # Set image and link file name.
    image_name = f"Chapter-{chapter}_image_{i}{file_extension}"
    image_path = os.path.join(chapterPath, image_name)

    os.makedirs(chapterPath, exist_ok=True)

    # Start download image;
    if os.path.exists(image_path):
        print(f"Image {image_name} already exists. Trying to check file integrity...")
        compare_result = main.compare_size(img, image_path, image_name, logfile)
        if compare_result is False:
            currentTime = gettime()
            main.write_file(logfile, f"{currentTime}: The size of image {img} from {chapterURL} not compared.\n")
    else:
        dl_result = main.dl_img(img, image_path, image_name, logfile)
        if dl_result is False:
            print(f"Error to downloading {url}.")
            currentTime = gettime()
            main.write_file(logfile, f"{currentTime}: Failed to download the image {img} from {chapterURL}.\n")
        else:
            print(f'{img} => {image_name}')
            compare_result = main.compare_size(img, image_path, image_name, logfile)
            if compare_result is False:
                currentTime = gettime()
                main.write_file(logfile, f"{currentTime}: The size of image {img} from {chapterURL} not compared.\n")

def findIMG(soup, chapterURL, readdiv, readjson, readencrypt, chapter, chapterPath, wait, logfile, debug):
    image_list = []
    if readjson is True:
        try:
            print(f"Trying to find images from {chapterURL}...")
            script = soup.find("script", string=re.compile(r'ts_reader\.run'))
            # Extract the JSON-like text from the script tag
            pattern = r'ts_reader\.run\((.+?)\)'
            match = re.search(pattern, script.string)
            if match:
                # Replace !1 with true and !0 with false
                json_text = match.group(1)
                json_text = re.sub(r'!1', 'true', json_text)
                json_text = re.sub(r'!0', 'false', json_text)
                json_data = json.loads(json_text)
                # Check for 'sources' in JSON data and extract image links
                if 'sources' in json_data and len(json_data['sources']) > 0:
                    image_list = json_data['sources'][0].get('images', [])
        except:
            currenttime = gettime()
            main.write_file(logfile, f"{currenttime}: Failed to find image urls from {chapterURL}.\n")
            return None
        
        return image_list
    elif readencrypt is True:
        count = main.countFiles(chapterPath)
        if count > 0:
            print("Already processed this chapter.")
            return None
        
        attempt = 0
        max_retries = 3

        for attempt in range(max_retries):
            try:
                options = Options()
                driver = webdriver.Chrome(options=options)
                driver.get(chapterURL)
                # Wait for the div to be present
                imgdiv = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, readdiv))
                )
                ranmouse(driver)
                time.sleep(wait)
                if debug is True:
                    main.waitforact()
                rmElements(driver, readdiv)
                dc_windowsize(driver)
                if debug is True:
                    main.waitforact()
                captureimg(driver, readdiv, chapter, chapterPath)
                driver.quit()

                if main.countFiles(chapterPath) > 0:
                    print("Screenshot successfully taken.")
                    return True
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(3)
                else:
                    currenttime = gettime()
                    main.write_file(logfile, f"{currenttime}: Failed to capture webpage from {chapterURL}.\n")
                    return None
    else:
        try:
            reader = soup.select_one(readdiv)
            imgtags = reader.find_all('img')
            image_list = [img['data-src'] if 'data-src' in img.attrs else img['src'] if 'src' in img.attrs else None for img in imgtags]
        except:
            currentTime = gettime()
            main.write_file(logfile, f"{currentTime}: Failed to find image urls from {chapterURL}.\n")
            return None
        
        return image_list
    
    
def rmElements(driver, readdiv):
    try:
        # Wait until the document.readyState is 'complete'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body/*')))
    except Exception as e:
        print(f"Page load timed out: {e}")

    try:
        # Wait for the div to be present
        target = driver.find_element(By.CSS_SELECTOR, readdiv)
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    # Traverse up the DOM tree to find all parent elements
    parent_elements = []
    parent_element = target
    while parent_element.tag_name != 'html':
        parent_element = parent_element.find_element(By.XPATH, '..')
        parent_elements.append(parent_element)
    
    # Hide all elements except the target div (using JavaScript)
    driver.execute_script("""
        var elements = document.querySelectorAll('*');
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.display = 'none';
        }
    """)
        
    # Show the target div and its parent elements
    driver.execute_script("""
        var targetDiv = arguments[0];
        targetDiv.style.display = 'block';
        var childNodes = targetDiv.getElementsByTagName('*');
        for (var i = 0; i < childNodes.length; i++) {
            if (childNodes[i].tagName.toLowerCase() !== 'script') {
                childNodes[i].style.display = 'block';
            }
        }
        var parentElements = arguments[1];
        for (var i = 0; i < parentElements.length; i++) {
            parentElements[i].style.display = 'block';
        }
    """, target, parent_elements)

    # Execute JavaScript to hide the scrollbar
    driver.execute_script(
        """
        var style = document.createElement('style');
        style.innerHTML = '::-webkit-scrollbar { display: none; }';
        document.head.appendChild(style);
        """
    )

    # Set width to auto for specified images
    driver.execute_script("""
        var windowWidth = window.innerWidth + 'px';
        var container = document.querySelectorAll('.container, #content, .wrapper, .postarea');
        container.forEach(function(div) {
            div.style.width = windowWidth;
            div.style.margin = 'unset';
            div.style.padding = 'unset';
        });
    """)

    driver.execute_script("""
        var images = document.querySelectorAll('img');
        images.forEach(function(img) {
            img.style.width = '100%';
            img.style.margin = 'unset';
            img.style.padding = 'unset';
        });
    """)

    driver.execute_script("""
        var container = document.querySelectorAll('.scrollToTop');
        container.forEach(function(div) {
            div.style.opacity = '0';
        });
    """)

def captureimg(driver, readdiv, chapter, chapterPath):
    try:
        # Wait for the div to be present
        target = driver.find_element(By.CSS_SELECTOR, readdiv)
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    # Get height of window
    height = driver.execute_script("return document.body.scrollHeight;")

    # Scroll down until the height no longer changes
    while True:
        # Scroll down by a certain amount
        driver.execute_script(f"window.scrollBy(0, {height});")

        time.sleep(2)
        
        # Calculate new total height
        new_height = driver.execute_script("return document.body.scrollHeight;")
        
        # Check if scrolling has reached the bottom of the page
        if new_height == height:
            break
        
        height = new_height
    
    # Return to top
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    # Calculate the number of images to capture
    image_height = driver.execute_script("return window.innerHeight;")
    total_height = target.size['height']
    num_images = (total_height + image_height - 1) // image_height
    os.makedirs(chapterPath, exist_ok=True)

    print(f"Image height: {image_height}")
    print(f"total height: {total_height}")
    print(f"total images: {num_images}")
    
    for i in range(num_images):
        if i != 0:
            # Scroll down by a certain amount
            driver.execute_script(f"window.scrollBy(0, {image_height});")
            time.sleep(0.6)
        # Save the image to a file
        image_path = os.path.join(chapterPath, f"Chapter-{chapter}_image_{i}.png")
        driver.save_screenshot(image_path)
        print(f"Saved to {image_path} successfully")

def ranmouse(driver):
    # Get the browser window size
    window_size = driver.get_window_size()
    max_x = window_size['width']
    max_y = window_size['height']

    # Generate random coordinates
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)

    # Create an ActionChains object
    actions = ActionChains(driver)

    # Move the mouse to the random coordinates
    actions.move_by_offset(x, y).perform()
    time.sleep(0.5)

def dc_windowsize(driver):
    # Get the current window size
    current_size = driver.get_window_size()

    # Decrease the width and height by 1 pixel
    width = current_size['width'] - 1
    height = current_size['height']

    # Set the new window size
    driver.set_window_size(width, height)
    time.sleep(1)

    # Get the current window size
    current_size = driver.get_window_size()

    # Decrease the width and height by 1 pixel
    width = current_size['width'] - 1
    height = current_size['height']

    # Set the new window size
    driver.set_window_size(width, height)
