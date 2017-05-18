# extracting all internal, unique links from a page in full-path format.
import os, sys, requests
from bs4 import BeautifulSoup, SoupStrainer
from urlparse import urljoin

def get_html(url):
    response = requests.get(url)
    html = response.content
    return html

def extract_all_link_tags(html):
    soup_object = BeautifulSoup(html, "html.parser")
    link_tags = soup_object.find_all("a")
    return link_tags

def extract_links(link_tags):
    links = []
    for tag in link_tags:
        try:
            links.append(tag["href"])
        except:
            pass
    return links

def extend_relative_paths(links):
    full_paths = []
    for each in links:
        full_path = urljoin(base_url, each)
        full_paths.append(full_path)
    return full_paths

def filter_out_external_links(links):
    internal_paths = []
    for link in links:
        if get_central_domain(link) == get_central_domain(base_url):
            internal_paths.append(link)
    return internal_paths

def filter_for_uniqueness(links):
    unique_links = set() # set ensures uniqueness
    for link in links:
        unique_links.add(link)
    return unique_links

# composite function
def crawl_site_for_links(url):
    html = get_html(url)
    link_tags = extract_all_link_tags(html)
    links = extract_links(link_tags)
    adjusted_links = extend_relative_paths(links)
    filtered_links = filter_out_external_links(adjusted_links)
    filtered_links = filter_for_uniqueness(filtered_links)
    return filtered_links
