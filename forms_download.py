from bs4 import BeautifulSoup
import requests
import re


req = requests.get("https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow=0&sortColumn=sortOrder&value=&criteria=&resultsPerPage=200&isDescending=false")
# Throw an error if website is inaccessible 
if req.status_code != 200:
    print("ERROR:", req.status_code)

soup = BeautifulSoup(req.text, "lxml")
# Scrape links to downloads
links = soup.find_all('a', class="LeftCellSpacer")

