import latest_user_agents
import requests as rq
from bs4 import BeautifulSoup as bs
import time
import os
import re
import json
import socket
import urllib.parse
from tqdm import tqdm

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

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"{path} have been created.")
    else:
        print(f"{path} is already exists.")

def write_file(filename, content):
    with open(filename, "a+", encoding='utf-8') as file:
        file.write(content)

def read_file(filepath):
    with open(filepath, "r", encoding='utf8') as file:
        return file.readlines()
    
def countFiles(path):
    files = os.listdir(path)
    file_count = len(files)

    return file_count

def manga_id(manga_url):
    # Define the simplified pattern to match the last part of the URL
    pattern = re.compile(r"([^/]+)/?$")
    # Parse the URL
    decode_url = urllib.parse.urlparse(manga_url)
    # Get the path part of the URL
    urlpath = decode_url.path
    # Search for the pattern in the path
    match = pattern.search(urlpath)
    # Extract the ID if a match is found
    if match:
        return match.group(1)
    else:
        return ''

def dl_img(url, path, title, logfile):
    get_datetime = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
    max_retries = 3  # Maximum number of download retries
    timeout = 90  # Set a timeout for the download
    headers = getHeaders()

    # Extract the host from the URL
    host = url.split('//')[1].split('/')[0]
    # Check if the host is online
    if not isonline(host):
        print(f"Host {host} is offline. Cannot download {url}.")
        write_file(logfile, f"{get_datetime}: Host {host} is offline. Cannot download {url}.\n")
        return None

    for i in range(max_retries):
        try:
            print(f"Start downloading {url}...")
            response = rq.get(url, headers=headers, stream=True, timeout=timeout)  # Send a GET request for the image
            response.raise_for_status()  # Raise an error for HTTP errors (status codes 4xx and 5xx)

            # Create the necessary directories to save the image file
            os.makedirs(os.path.dirname(path), exist_ok=True)

            # Write the received content in chunks to the specified file path
            total_size = int(response.headers.get('content-length', 0))  # Total size of the file
            with open(path, 'wb') as file, tqdm(
                desc=title,
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
                disable=not total_size,
            ) as bar:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
                        file.flush()
                        bar.update(len(chunk))  # Update progress bar
        except rq.exceptions.RequestException as e:
            if i == max_retries - 1:  # If it's the final retry attempt and failed
                print(f"Error {e} occurred while downloading {url}.")
                write_file(logfile, f"{get_datetime}: Error {e}. Failed to download {url}.\n")  # Log the error in a file
                download = False
            else:
                print(f"Error {e} occurred while downloading {url}. Retrying...")  # Retry the download
            time.sleep(2)  # Wait for 2 seconds before retrying
        else:
            download = True
            break
    else:
        print(f"Can't download {url} with max retries.")
        write_file(logfile, f"{get_datetime}: Can't download {url} with max retries.\n")
        download = False
    
    return download

def isonline(host, port=443, timeout=10):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(f"Host {host} is offline: {ex}")
        return False

def check_integrity(url):
    # Fetch the user agent for the request
    timeout = 30  # Set a timeout value for the request
    headers = getHeaders()
    
    try:
        # Send a HEAD request to the URL with specified headers and timeout
        response = rq.head(url, headers=headers, timeout=timeout)
        
        # If the response status code is 200 (OK)
        if response.status_code == 200:
            # Get the content size from the response headers, default to 0 if not available
            content_size = int(response.headers.get('Content-Length', 0))
    except rq.exceptions.RequestException as e:
        # In case of an exception during the request, handle the error
        print(f"Error {e} occurred while checking integrity of {url}.")
        content_size = ''  # Set content_size as an empty string in case of error

    return content_size

def compare_size(url, path, title, log_path):
    print(f"Comparing size {path} with {url}...")
    try:
        content_size = check_integrity(url)
        print(f"Image size from {url} is {content_size} bytes.")
    except:
        content_size = ''

    if content_size:
        if os.path.exists(path):
            local_file_size = os.path.getsize(path)
            if content_size == local_file_size:
                print("Image file size and content size are matched.")
                match = True
            else:
                print("Image file size and content size do not match.")
                print(f"Image file size: {local_file_size} bytes")
                print(f"Content size: {content_size} bytes")
                print(f"Trying to download {url} again...")
                os.remove(path)
                dl = dl_img(url, path, title, log_path)
                if dl == True:
                    match = True
                else:
                    match = False
    else:
        match = False
    return match

def findchapternum(title):
    # Extract text content from the BeautifulSoup Tag object
    if 'ตอน' in title:
        result = re.split(r'(?=ตอน)', title)[-1]
    
    if 'Chapter' in title:
        result = re.split(r'(?=Chapter)', title)[-1]


    # Use regular expression to find all groups of digits in the input string
    numbers = re.findall(r'\d+', result)

    # If there are two numbers, format them as "x-y-z"
    if len(numbers) == 3:
        return '-'.join(numbers)
    
    # If there are two numbers, format them as "x-y"
    if len(numbers) == 2:
        return '-'.join(numbers)
    
    # If there's only one number, return it as is
    if len(numbers) == 1:
        return numbers[0]
    
    # If there are no numbers, return an empty list
    if not numbers:
        return ''
    
def getchapter(title, chapter_title):
    # Escape special characters in the title
    pattern = re.escape(title)

    # Use re.sub to remove the title from the chapter_title
    text = re.sub(f"^{pattern}", "", chapter_title).strip()

    # Use regular expression to find all groups of digits in the input string
    numbers = re.findall(r'\d+', text)

    # If there are two numbers, format them as "x-y-z"
    if len(numbers) == 3:
        return '-'.join(numbers)
    
    # If there are two numbers, format them as "x-y"
    if len(numbers) == 2:
        return '-'.join(numbers)
    
    # If there's only one number, return it as is
    if len(numbers) == 1:
        return numbers[0]
    
    # If there are no numbers, return an empty list
    if not numbers:
        return ''
    

def extract_num(first_chapter, title, url):
    data_num = ''
    try:
        data_str = first_chapter['data-num']
        numeric_part = re.search(r'[\d.]+', data_str)
        if numeric_part:
            data_num = int(float(numeric_part.group()))
            return data_num
    except:
        pass
    
    if not data_num:
        try:
            a_tag = first_chapter.find('a')
            a_title = a_tag.text.strip()
            if not a_title:
                a_title = a_tag['title']
            # Remove invalid characters;
            a_title = re.sub(r'[\\/:"*?<>|]', '', a_title)
            strip = a_title.replace(title, '')
            match = re.search(r'\d+', strip)
            if match:
                data_num = int(match.group())
                return data_num
        except:
            return None
        
def waitforact():
    print("Press Enter to continue or ESC to exit...")
    while True:
        user_input = input()
        if user_input == '':
            print("Continuing to the next step...")
            break
        elif user_input.lower() == 'esc':
            print("Exiting...")
            return False
    return True

def savejson(filename, mgTitle=None, mgtype=None, mggenres=None, mgstatus=None, chaptercount=None, chaptertitle=None, chapterurl=None):
    # Set prefixes to be used for fetch and save data file;
    title_prefix = "Title"
    type_prefix = "Type"
    genre_prefix = "Genres"
    status_prefix = "Status"
    count_prefix = "Count"
    savechapters = "ChapterURLs"

    # Initialize data with existing file contents if it exists
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        data = {
            title_prefix: mgTitle,
            type_prefix: mgtype,
            genre_prefix: mggenres,
            status_prefix: mgstatus,
            count_prefix: chaptercount,
            savechapters: {}
        }

    # Update the data with the new values if provided
    if mgTitle is not None:
        data[title_prefix] = mgTitle
    if mgtype is not None:
        data[type_prefix] = mgtype
    if mggenres is not None:
        data[genre_prefix] = mggenres
    if mgstatus is not None:
        data[status_prefix] = mgstatus
    if chaptercount is not None:
        data[count_prefix] = chaptercount

    # Check if chaptertitle and chapterurl are provided
    if chaptertitle and chapterurl:
        # Check if the chapter URL already exists
        if chapterurl not in data[savechapters]:
            data[savechapters][chapterurl] = chaptertitle
        else:
            print(f"Chapter URL '{chapterurl}' already exists. Skipping addition.")

    # Open the data file in write mode
    with open(filename, "w", encoding="utf-8") as file:
        # Write the data to the file
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Save data to {filename} successfully.")

def readjson(filename):
    # Open the data file in read mode
    with open(filename, "r", encoding="utf-8") as file:
        # Read the data from the file
        data = json.load(file)
    
    mgtitle = data["Title"]
    mgtype = data["Type"]
    mggenres = data["Genres"]
    mgStatus = data["Status"]
    chaptercount = data["Count"]
    chapterurls = data["ChapterURLs"]

    return mgtitle, mgtype, mggenres, mgStatus, chaptercount, chapterurls