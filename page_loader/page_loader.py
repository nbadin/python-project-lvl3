from bs4 import BeautifulSoup
import requests
import os
from page_loader.src.get_names import get_basic_name
from page_loader.src.images import dowload_image


def download(url, path=os.getcwd()):
    dir_path_for_files = f'{get_basic_name(url)}_files'
    os.makedirs(dir_path_for_files)
    filepath = f'{get_basic_name(url)}.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        image_path = dowload_image(image['src'], dir_path_for_files)
        image['src'] = image_path

    with open(filepath, 'w') as f:
        f.write(soup.prettify())

    return filepath
