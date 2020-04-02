import requests
from requests.exceptions import HTTPError
url = 'http://gilbertduenas.com/'
try:
    response = requests.get(url)
    # Exception check
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error: {http_err}')  
except Exception as err:
    print(f'Other error: {err}')  
else:
    print('Success!')