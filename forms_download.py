from bs4 import BeautifulSoup
import requests
from time import time


# Fetch all the URLs from the website to download PDFs, within a range of years
def get_links(year_range: range, url:str):
    # Create a session for getting data 
    session = requests.session()
    session.proxies = {}
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    session.headers = {'user-agent': user_agent}
    # scarpe the website
    req = session.get(url, stream=False)
    # Throw an error if website is inaccessible
    if req.status_code != 200:
        print("ERROR:", req.status_code)
    soup = BeautifulSoup(req.content, features="lxml")
    links = []
    # Get the values from the "Revision Date" field, strip out the markup, and append to a list
    for row in soup.select('tr.even'):
        year = int(row.select('td.EndCellSpacer')[0].text.strip())
        link = row.select('td.LeftCellSpacer a[href]')[0]['href']
        if year in year_range:
            links.append(link)
            return links


# Download the files, using the values returned by the above function    
def download_pdfs(links: list):

    # Get dates from the "Revision Date" field on website
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


download_pdfs(get_links((2012, 2017), "https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow=0&sortColumn=sortOrder&value=&criteria=&resultsPerPage=200&isDescending=false"))
