import os, sys, requests
from bs4 import BeautifulSoup, SoupStrainer
from random import randint
from urlparse import urljoin
from general_helpers import *
from link_extraction_helpers import *

# initial page to crawl
if len(sys.argv) == 2:
    url = sys.argv[1]
    base_url = url
    project_file = os.getcwd() + "/output_files/" + get_central_domain(url)
else:
    url = "https://pythonprogramming.net" # default
    base_url = url
    project_file = os.getcwd() + "/output_files/" + get_central_domain(url)

def create_output_directory():
    if not os.path.exists(os.getcwd() + "/output_files"):
        os.mkdir("output_files")

def create_project_file(file_name):
    if os.path.exists(project_file):
        os.remove(project_file)
    with open(project_file, 'w') as f:
        f.write(file_name)

create_output_directory()
create_project_file(url)

with open(project_file, "r+") as project_file:
    lines = project_file.readlines()
    links = crawl_site_for_links(lines[0])
    for each in links:
        project_file.write(each + "\n")


