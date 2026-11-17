# File name: esv_test.py
# Jay Ueki
# Test the ESV API out: does the footnote include references, or is it just the additional information?

import re
import random
import requests
import pandas as pd

API_KEY = 'c8fcdaf43496dce4ed6e738aec110307e5e75437'
API_URL = 'https://api.esv.org/v3/passage/text/'

headers = {
    'Authorization': f'Token {API_KEY}'
}

params = {
    'q': "Matthew 21:42",
    'include-footnotes': True,
    'include-footnote-body': True
}


if __name__ == '__main__':
    response = requests.get(API_URL, params=params, headers = headers)
    print(response.json()['passages'])