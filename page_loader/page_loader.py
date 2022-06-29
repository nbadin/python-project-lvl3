import requests
import re
import os
from bs4 import BeautifulSoup


def download(url, path=os.getcwd()):
    response = requests.get(url)

    if response.ok:
        filename = make_name(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        filepath = f'{path}/{filename}'
        with open(filepath, 'w') as f:
            f.write(soup.prettify())

        return filepath

    else:
        raise ValueError(
            f'Page wasn\'t downloaded! Response code: {response.status_code}'
        )


def make_name(url):
    name_without_scheme = re.sub(r'^(http://|https://)', '', url)
    name_without_ext = re.sub(r'\.html', '', name_without_scheme)

    return '-'.join(re.split(r'\W', name_without_ext)) + '.html'
