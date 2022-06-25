from page_loader.page_loader import download
import tempfile
import os



def test_download(requests_mock):
    requests_mock.get('http://test.com', text='data')
    tmp_path = tempfile.mkdtemp()
    path_to_file = download('http://test.com', tmp_path)
    assert os.path.isfile(path_to_file)
    with open(path_to_file) as f:
        text = f.read()
        assert text == 'data'
