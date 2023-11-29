import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Prompt for base URL and maximum redirects
base_url = input("Enter the base URL (https://exapmple.com/): ")
max_redirects = int(input("Enter the maximum number of redirects: "))

# Add a trailing slash if not present in the base URL
if not base_url.endswith('/'):
    base_url += '/'

base_dir = './downloaded_files'

# Create base directory if it doesn't exist
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

def extract_links(soup):
    links = set()
    for link in soup.find_all('a', href=True):
        link_url = urljoin(base_url, link['href'])
        links.add(link_url)
    return links

def download_resources(resources):
    for res_url in resources:
        try:
            response = requests.get(res_url, allow_redirects=False)
            if response.status_code == 200:
                res_name = res_url.split(base_url)[-1]  # Extract relative path
                res_dir = os.path.dirname(res_name)
                res_path = os.path.join(base_dir, res_dir)

                if not os.path.exists(res_path):
                    os.makedirs(res_path)

                with open(os.path.join(base_dir, res_name), 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded: {res_name}")

                if response.history and len(response.history) <= max_redirects:
                    redirect_url = response.headers['Location']
                    redirect_url = urljoin(base_url, redirect_url)
                    download_resources({redirect_url})  # Follow redirects recursively

            else:
                print(f"Error downloading - Status Code: {response.status_code} - URL: {res_url}")

        except Exception as e:
            print(f"Error downloading: {str(e)}")

try:
    response = requests.get(base_url, allow_redirects=False)
    if response.status_code == 200:
        html_data = response.text
        soup = BeautifulSoup(html_data, 'html.parser')

        # Extract links from the initial HTML
        all_links = extract_links(soup)

        # Find additional links recursively
        download_resources(all_links)

        # Save the HTML content
        with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as file:
            file.write(html_data)
        print('HTML response saved in index.html')

    else:
        print(f"Error fetching data - Status Code: {response.status_code}")

except Exception as e:
    print(f"Error fetching data: {str(e)}")
