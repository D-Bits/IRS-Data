"""
Script for scraping IRS form meta data.
"""
import pandas as pd


def get_metadata(url):

    try:
        # Load the HTML from the URL into Pandas
        data = pd.read_html(url)
        # Convert the above list variable to a DataFrame, so it can be dumped to JSON.
        df = pd.DataFrame(data)
        # Dump the JSON a file in the "dumps" directory. 
        df.to_json("./dumps/irs_forms.json", orient="records")
    except:
        print("An error has occured. We apologize for the inconvience.")


get_metadata("https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow=0&sortColumn=sortOrder&value=&criteria=&resultsPerPage=200&isDescending=false")

    