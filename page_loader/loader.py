from distutils.debug import DEBUG
from page_loader.PageLoader import PageLoader
import logging


logging.basicConfig(level=DEBUG)


def download(url, path):
    try:
        page = PageLoader(url, path)
        filepath = page.download()
        return filepath
    except Exception as err:
        logging.exception(err)
