from page_loader.page_loader import download
import tempfile
import os
import pytest


@pytest.fixture
def downloaded_page():
    with open('tests/fixture/page.html', 'r') as f:
        text = f.read()
        return text


def test_download(requests_mock, downloaded_page):
    requests_mock.get('http://test.com', text=downloaded_page)
    tmp_path = tempfile.mkdtemp()
    path_to_file = download('http://test.com', tmp_path)
    assert os.path.isfile(path_to_file)
    with open(path_to_file) as f:
        text = f.read()
        assert text == downloaded_page
