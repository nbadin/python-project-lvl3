import os
import argparse
from page_loader.loader import download


def main():
    parser = argparse.ArgumentParser(
        prog='page-loader',
        description='Load page from url',
        usage='pageloader [--output dirpath] url'
    )

    parser.add_argument('--output', default=os.getcwd())
    parser.add_argument('url')

    args = parser.parse_args()
    download(args.url, args.output)
