import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re



def download(url, path=os.getcwd()):
    response = requests.get(url)

    if response.ok:
        filename = f'{make_name(url)}'
        host = urlparse(url).netloc
        soup = BeautifulSoup(response.text, 'html.parser')
        dir_name =os.path.join(path, make_name(url, dir=True))
        os.mkdir(dir_name)
        resorces = get_resorces(soup, host=host)
        filepath = f'{path}/{filename}'
        with open(filepath, 'w') as f:
            f.write(soup.prettify())

        return filepath

    else:
        raise ValueError(
            f'Page wasn\'t downloaded! Response code: {response.status_code}'
        )


def make_name(url, *, dir=False):
    if dir:
        tail = '_files'
    elif re.search(r'\.\w+$', url) is None:
        tail = '.html'
    else:
        tail = re.search(r'\.\w+$', url).group(0)

    name_without_scheme = re.sub(r'^(http://|https://)', '', url)

    if name_without_scheme.endswith(tail):
        name_without_scheme = name_without_scheme.replace(tail, '')

    new_name = '-'.join(re.split(r'\W', name_without_scheme))
    return f'{new_name}{tail}'


def get_resorces(soup, *, host=None):
    items = soup.find_all('img', src=True) + soup.find_all('link', href=True) + soup.find_all('script', src=True)
    filtered_items = []
    for item in items:
        url = item['href'] if item.name == 'link' else item['src']
        if item.name == 'img':
            filtered_items.append(item)
        elif urlparse(url).netloc == host:
            filtered_items.append(item)
    
    return filtered_items

