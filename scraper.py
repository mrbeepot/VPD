import requests
from bs4 import BeautifulSoup as BS
import pathlib
import os
from multiprocessing import Process


def download_helper(ids, file_names, urls, base_dir):
    for id, file_name, url in zip(ids, file_names, urls):
        print("ID = " + str(id.text))
        print("Source URL = " + str(url.text))
        download(url, base_dir, file_name)


def check_if_video_exists(base_dir, file_name):
    path = str(base_dir + file_name.text)
    print(path)
    file = pathlib.Path(path)
    print(str(file.name))
    return file.exists()


def download(url, base_dir, file_name):
    if not check_if_video_exists(base_dir, file_name):
        r = requests.get(url.text, stream=True, allow_redirects=True)
        print("actual url = " + str(r.url))
        with open(base_dir + file_name.text, "wb") as video:
            print("Saving as file = " + str(file_name.text))
            for chunk in r.iter_content(chunk_size=1024):
                video.write(chunk)
            print("Saved\n")
    else:
        print(file_name.text + " already exists. Skipping")


def estimate_size_of_video_file(url):
    size = requests.head(url.text).headers['Content-Length']
    print("size : " + str(size))


def main():
    with open("sample-dataset.xml", "r") as dataset_xml_file:
        soup = BS(dataset_xml_file, "lxml")
        ids = soup.find_all("id")
        file_names = soup.find_all("filename")
        urls = soup.find_all("source")
        base_dir = "videos/"
        download_helper(ids=ids, file_names=file_names, urls=urls, base_dir=base_dir)


main()
