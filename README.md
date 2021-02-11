# IRS-Data

A tool to scrape data for IRS forms from their [website](https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow=25&sortColumn=sortOrder&value=&criteria=&resultsPerPage=25&isDescending=false). Built using Python 3, and Scrapy.

## Project Setup

*You need to following software installed before going further.*

- Python 3
- Pip3

### Setup Steps

- Clone this repository
- Create a virtualenv by running `python3 -m venv env`
- Activate venv:
    * `source env/bin/activate` on Unix-like systems
    * `env/scripts/activate` on Windows
- Install dependencies by running `pip install -r requirements.txt`.

Assuming you were able to complete all the above steps without problems, you should be ready to run the program.

## File Guide

- `forms_data.py`: Get meta data for the IRS forms.
- `forms_download.py`: Download files within a specific data range. 

To scrape data, make sure your venv is active, and run the Python scripts in the repository with `python3 <file_name>`.
