import requests
import os
from urllib.parse import urlparse


def get_picture(url, directory):
    filename = urlparse(url).path.split('/')[-1]
    response = requests.get(url)
    response.raise_for_status()

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(f'images/{filename}', 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    get_picture(
        'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 
        'images')
