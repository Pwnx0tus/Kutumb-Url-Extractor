# FIX THIS:
# remove duplicates, list ko sort karo, ya tuple use kro.
# url work nahi kar rha tha jo mene thik kiya he
# you made a single url crawler, not website crawler. use loop, after extracting urls from href, src, etc attributes, again pass extracted url list to the same loop, do this untill every single url of website is printed out.
# use multithreading for fast results

import requests
import bs4
import os
import concurrent.futures
try:
  import requests
  import requests
except ImportError:
  os.system("clear")
  os.system("pip install requests")
  os.system("clear")
  os.system("pip install requests")
try:
  from colorama import *
  from colorama import *
except ImportError:
  os.system("clear")
  os.system("pip install colorama")
  os.system("clear")
  os.system("pip install colorama")
import time


os.system("clear")
auth = """

=================+===================
| |/ /   _| |_ _   _ _ __ ___ | |__  
| ' / | | | __| | | | '_ ` _ \| '_ \ 
| . \ |_| | |_| |_| | | | | | | |_) |
|_|\_\__,_|\__|\__,_|_| |_| |_|_.__/ 
=================+===================
    Kutumb Url Extractor 
    Team:SHELL SQUAD
    Developer:TR TROJAN 
    VERSION:0.5 BETA
                        """

print(Style.BRIGHT)
print(Fore.GREEN + auth)


print(Fore.GREEN + auth)


def extract_urls(url):
    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        hrefs = []
        img_links = []
        meta_tags = []
        # Find all <a>, <img>, and <meta> tags:
        for tag in soup.find_all(['a', 'img', 'meta']):
            # Extract the URL, if it exists:
            if tag.has_attr('href'):
                hrefs.append(tag['href'])
            elif tag.has_attr('src'):
                img_links.append(tag['src'])
            elif tag.has_attr('content'):
                meta_tags.append(tag['content'])
        return hrefs, img_links, meta_tags
    except:
        print("An error occurred while extracting URLs.")
        return [], [], []

# Prompt the user for a website URL:
url = input("Enter a website URL: ")
if not url.startswith("http://") and not url.startswith("https://"):
    url="http://"+url
if url.endswith("/"):
    url=url[:-1]
print("[+] Target: "+url)
    
    
# Extract URLs from the webpage:
hrefs, img_links, meta_tags = extract_urls(url)

# Print the URLs for each section:
print("Found {} standard links:".format(len(hrefs)))
for webs in hrefs:
    print(url+webs)

print("\nFound {} image links:".format(len(img_links)))
for link in img_links:
    print(url+link)

print("\nFound {} meta tags:".format(len(meta_tags)))
for tag in meta_tags:
    print(tag)
