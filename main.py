import os, sys, requests
from bs4 import BeautifulSoup, SoupStrainer
from urlparse import urljoin
from helpers import *

# starting page
if len(sys.argv) == 2:
    url = sys.argv[1]
    base_url = url
else:
    # default
    url = "https://thenewboston.com"
    base_url = url

def get_html(url):
    response = requests.get(url)
    html = response.content
    return html

def extract_all_link_tags(html):
    soup_object = BeautifulSoup(html, "html.parser")
    a_tags = soup_object.find_all("a")
    return a_tags

def extract_hrefs(a_tags):
    links = []
    for tag in a_tags:
        try:
            links.append(tag["href"])
        except:
            print('failure to add one.')
    return links

def extend_relative_paths(links):
    full_paths = []
    for each in links:
        full_path = urljoin(base_url, each)
        full_paths.append(full_path)
    return full_paths

def remove_external_links(links):
    internal_paths = []
    for link in links:
        if get_central_domain(link) == get_central_domain(base_url):
            internal_paths.append(link)
    return internal_paths

def filter_for_uniqueness(links):
    unique_links = set()
    for link in links:
        unique_links.add(link)
    return unique_links

output = get_html(url)
output = extract_all_link_tags(output)
output = extract_hrefs(output)
output = extend_relative_paths(output)
output = remove_external_links(output)
output = filter_for_uniqueness(output)
for each in output:
    print(each)

"""
- git etc
- url
- trying safely
- trying output
"""
