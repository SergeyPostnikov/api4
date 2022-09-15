import requests
import os
from os.path import splitext
from urllib.parse import urlparse, unquote
from datetime import datetime


def get_filename(url):
    return unquote(urlparse(url).path.split('/')[-1])


def get_ext(url):
    return splitext(get_filename(url))[1]


def get_date(datestring):
    dt = datetime.strptime(datestring, '%Y-%m-%d %H:%M:%S')
    return dt.strftime("%Y/%m/%d")


def get_picture(url, directory, params={}):
    response = requests.get(url, params=params)
    response.raise_for_status()

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(f'images/{get_filename(url)}', 'wb') as file:
        file.write(response.content)
