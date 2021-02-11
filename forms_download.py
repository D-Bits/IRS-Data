from bs4 import BeautifulSoup
import requests
import re


def get_links(url):

    session = requests.session()
    session.proxies = {}
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    session.headers = {'user-agent': user_agent}
    req = session.get(url, stream=False)
    
    print(f'{req.text}')
    # Throw an error if website is inaccessible 
    if req.status_code != 200:
        print("ERROR:", req.status_code)

    return req


def download_pdfs(links):

    soup = BeautifulSoup(links.text, "lxml")
    # Scrape links to downloads
    links = soup.find('td', attrs={'class': "LeftCellSpacer"})
    children = links.findChildren("a", recursive=False)
    #print(links)
    for a in children:
        res = requests.get(a, stream=True)
        print(res.status_code)
        with open(f"./pdfs/{a}.pdf") as f:
            f.write(res.content)
    #downloads = requests.get(links)


download_pdfs(get_links("https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow=0&sortColumn=sortOrder&value=&criteria=&resultsPerPage=200&isDescending=false"))
