import argparse
import requests

from picture_handlers import get_picture


def get_spacex_links(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    try:
        return response.json()['links']['flickr']['original']
    except KeyError:
        print('No links taken\n check api response')
        return []


def fetch_spacex_launch(launch_id):
    for url in get_spacex_links(launch_id):
        get_picture(url, 'images')
        print('fetch')


if __name__ == '__main__':
    # for test use --launch_id 5eb87d47ffd86e000604b38a
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', help='launch id', default='latest')
    args = parser.parse_args()
    fetch_spacex_launch(args.launch_id)
    print(get_spacex_links(args.launch_id))
