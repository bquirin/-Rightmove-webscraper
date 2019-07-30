import requests
from bs4 import BeautifulSoup
import csv


def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    if not response.ok:
        print(f"Server responded with {response.status_code}")
    return soup


def get_data(soup):
    all_houses = []
    divs = soup.findall("div", class_="test")
    for div in divs:
        all_houses.append({
            "title": div.find("h1").text,
            "price": div.find("h2").text

        })

    return all_houses


def main():
    url = "https://www.rightmove.co.uk/"
    webpage = get_page(url)
    print(get_data(webpage))


if __name__ == "__main__":
    main()
