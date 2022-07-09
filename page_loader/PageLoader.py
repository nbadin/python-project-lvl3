import logging
import requests
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urlparse


class PageLoader:
    def __init__(self, url, path=os.getcwd()):
        self.url = url
        self.path = path
        self.__filename = self.__make_name(self.url)
        self.__page = BeautifulSoup(self.__load_page_content(), 'html.parser')
        self.host = urlparse(self.url).netloc

    @property
    def content(self):
        return self.__page.prettify

    @property
    def filename(self):
        return self.__filename

    def download(self):
        self.dirpath = self.__make_dir()
        self.__download_img()
        self.__download_links()
        self.__download_scripts()
        filepath = os.path.join(self.path, self.filename)
        open(filepath, 'w').write(self.content())
        return filepath

    def __download_img(self):
        images = self.__page.find_all('img', src=True)
        for img in images:

            response = requests.get(img['src'])
            if response.ok:

                filename = self.__make_name(img['src'])
                filepath = os.path.join(self.dirpath, filename)
                open(filepath, 'wb').write(response.content)
                img['src'] = os.path.join(self.resources_dirname, filename)

            else:
                raise ValueError(
                    f'Files wasn\'t downloaded! Response code: {response.status_code}'  # noqa: E501
                )

    def __download_links(self):
        links = self.__page.find_all('link', href=True)
        for link in links:

            if urlparse(link['href']).netloc == self.host:
                response = requests.get(link['href'])

                if response.ok:
                    filename = self.__make_name(link['href'])
                    filepath = os.path.join(self.dirpath, filename)
                    open(filepath, 'w').write(response.text)
                    link['href'] = os.path.join(self.resources_dirname, filename)  # noqa: E501
                else:
                    raise ValueError(
                        f'Files wasn\'t downloaded! Response code: {response.status_code}'  # noqa: E501
                    )

    def __download_scripts(self):
        scripts = self.__page.find_all('script', src=True)
        for script in scripts:

            if urlparse(script['src']).netloc == self.host:
                response = requests.get(script['src'])

                if response.ok:
                    filename = self.__make_name(script['src'])
                    filepath = os.path.join(self.dirpath, filename)
                    open(filepath, 'wb').write(response.content)
                    script['src'] = os.path.join(self.resources_dirname, filename)  # noqa: E501

                else:
                    raise ValueError(
                        f'Files wasn\'t downloaded! Response code: {response.status_code}'  # noqa: E501
                    )

    def __load_page_content(self):
        response = requests.get(self.url)
        if response.ok:
            return response.text
        else:
            raise ValueError(
                f'Page wasn\'t downloaded! Response code: {response.status_code}'  # noqa: E501
            )

    def __make_name(self, url):
        if re.search(r'\.\w+$', url) is None:
            tail = '.html'
        else:
            tail = re.search(r'\.\w+$', url).group(0)
        name_without_scheme = re.sub(r'^(http://|https://)', '', url)

        if name_without_scheme.endswith(tail):
            name_without_scheme = name_without_scheme.replace(tail, '')

        new_name = '-'.join(re.split(r'\W', name_without_scheme))

        return f'{new_name}{tail}'

    def __make_dir(self):
        self.resources_dirname = f'{self.filename.split(".")[0]}_files'
        dirpath = os.path.join(self.path, self.resources_dirname)
        os.mkdir(dirpath)
        logging.info(f'Create dir {dirpath}')
        return dirpath
