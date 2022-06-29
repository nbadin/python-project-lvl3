from bs4 import BeautifulSoup
import requests
import os
from page_loader.src.get_names import get_image_name


def get_images_list(path):
    with open(path, 'r') as f:
        text = f.read()

        soup = BeautifulSoup(text, 'html.parser')
        return map(lambda x: x.get('src'), soup.find_all('img'))


def dowload_image(url, path):
    response = requests.get(url)
    file_path = os.path.join(path, get_image_name(url))
    with open(file_path, 'wb') as f:
        f.write(response.content)

    return file_path
