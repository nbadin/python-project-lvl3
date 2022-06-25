import requests
import os


def download(url, path=os.getcwd()):
    response = requests.get(url)
    filepath = os.path.join(path, get_html_file_name(url))

    with open(filepath, 'w') as f:
        f.write(response.text)

    return filepath


def get_basic_name(url):
    if 'http://' in url:
        basic_name = url[7:]
    elif 'https://' in url:
        basic_name = url[8:]
    return basic_name.replace('.', '-').replace('/', '-')


def get_html_file_name(url):
    return f'{get_basic_name(url)}.html'
