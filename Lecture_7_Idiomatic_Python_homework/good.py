"""
NHTSA has a public api; the url we will be working with is 
https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json&page=1

This api endpoint returns JSON; it has the field 'Results' - a list of car manufacturers with details.
We want to create a dictionary with country as a key, and list of manufacturer names as a value, e.g:
{
    'USA': ['Tesla', 'Ford', ...],
    'Japan': ['Honda', 'Subaru', ...]
}
Use 'Mfr_Name' as a manufacturer name.
If 'Country' is empty - skip it. We should traverse through all pages of this api endpoint

bad.py has a finished implementation of this task. Your goal is to make this code better, in any
way you can think of. Put your solution in good.py
Some examples of what can be done:
- you can create your own iterator/generator to go through pages for you
- insertion of items into dictionary can be improved

Also, add more tests to the test_dict.py to check response content.
"""
import logging
from typing import Dict, List
from collections import defaultdict
import requests

logging.basicConfig(level=logging.INFO)


def create_country_make_dict(url: str) -> Dict[str, List[str]]:
    country_manufacturers: Dict[str, List[str]] = defaultdict(list)
    for country, manufacturer in manufactures(url):
        country_manufacturers[country].append(manufacturer)

    return country_manufacturers


def manufactures(url: str):
    page = 1
    while True:
        response = requests.get(f"{url}&page={page}")
        make_dict = response.json()
        if not make_dict["Count"]:
            break
        for manufacturer in make_dict["Results"]:
            country = manufacturer["Country"]
            if country:
                yield country, manufacturer["Mfr_Name"]
        logging.info(f"Done with page {page}")
        page += 1
