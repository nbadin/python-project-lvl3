def get_basic_name(url):
    if 'http://' in url:
        basic_name = url[7:]
    elif 'https://' in url:
        basic_name = url[8:]
    if url.endswith('.html'):
        basic_name = basic_name[:-5]
    return basic_name.replace('.', '-').replace('/', '-')


def get_image_name(url):
    *parts, ext = url.split('.')
    return f"{get_basic_name('.'.join(parts))}.{ext}"
