import pandas as pd


url = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow=0&sortColumn=sortOrder&value=&criteria=&resultsPerPage=200&isDescending=false"

data = pd.read_html(url)
df = pd.DataFrame(data, columns=['Index', 'Product Number', 'Title', 'Revision Date'])
json_data = df.to_json("./dumps/irs_forms.json", orient="records")
print(df)