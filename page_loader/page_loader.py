import requests
import os


def download(url, path=os.getcwd()):
    response = requests.get(url)
    filepath = os.path.join(path, build_filename(url))

    with open(filepath, 'w') as f:
        f.write(response.text)

    return filepath


def build_filename(url):
    if 'http://' in url:
        return '.'.join([url[7:].replace('.', '-').replace('/', '-'), 'html'])
    elif 'https://' in url:
        return '.'.join([url[8:].replace('.', '-').replace('/', '-'), 'html'])
