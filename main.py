import requests
import os

directory = 'images'
filename = 'hubble.jpeg'
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
response = requests.get(url)
response.raise_for_status()

if not os.path.exists(directory):
    os.makedirs(directory)

with open(f'images/{filename}', 'wb') as file:
    file.write(response.content)
