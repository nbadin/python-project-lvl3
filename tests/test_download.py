from page_loader import download
import tempfile
import os
import pytest


@pytest.fixture
def downloaded_page():
    with open('tests/fixture/page.html', 'r') as f:
        text = f.read()
        return text


@pytest.fixture
def downloaded_image():
    with open('tests/fixture/files/img.svg', 'rb') as f:
        content = f.read()
        return content


def test_download(requests_mock, downloaded_page, downloaded_image):
    requests_mock.get('http://test/basic', text=downloaded_page)
    requests_mock.get('http://test/files/img.svg', content=downloaded_image)
    tmp_path = tempfile.mkdtemp()
    path_to_file = download('http://test/basic', tmp_path)
    assert os.path.isfile(path_to_file)
    assert os.path.join(tmp_path, 'test-basic.html') == path_to_file
    with open(path_to_file) as f:
        text = f.read()
        #assert text == downloaded_page
