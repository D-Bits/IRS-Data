from bs4 import BeautifulSoup
import requests
import re


def download_files(url):

    req = requests.get(url, stream=True)
    # Throw an error if website is inaccessible 
    if req.status_code != 200:
        print("ERROR:", req.status_code)

    soup = BeautifulSoup(req.text, "lxml")
    # Scrape links to downloads
    #links = soup.find_all('td', attrs={'class': "LeftCellSpacer"})
    #print(links)
    for a in soup.select('.LeftCellSpacer td a'):
        res = requests.get(a, stream=True)
        print(res.status_code)
        with open(f"./pdfs/{a}.pdf") as f:
            f.write(res.content)
    #downloads = requests.get(links)


download_files("https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow=0&sortColumn=sortOrder&value=&criteria=&resultsPerPage=200&isDescending=false")