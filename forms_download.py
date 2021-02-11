from bs4 import BeautifulSoup
import requests
from time import time


def get_links(url):
    session = requests.session()
    session.proxies = {}
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    session.headers = {'user-agent': user_agent}
    req = session.get(url, stream=False)
    # Throw an error if website is inaccessible
    if req.status_code != 200:
        print("ERROR:", req.status_code)
    soup = BeautifulSoup(req.content, features="lxml")
    links = [l['href'] for l in soup.select('td.LeftCellSpacer a[href]')]
    # with open('to_download.csv', 'a+') as to_download:
    #     writer = csv.writer(to_download)
    #     for l in links:
    #         writer.writerow(l)
    return links
def download_pdfs(links):
    for url in links:
        try:
            r = requests.get(url, allow_redirects=True)
            open(f'{url.split("/")[-1]}', 'wb').write(r.content)
            time.sleep(1) #take it easy on the IRS
        except:
            print(f'failure on {url}')
def follow_nextpage_link():
    # get the next page of links and add them to the list
    pass


download_pdfs(get_links("https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow=0&sortColumn=sortOrder&value=&criteria=&resultsPerPage=200&isDescending=false"))
