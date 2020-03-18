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
    divs = soup.find_all("div", class_="l-searchResult is-list is-not-grid")
    for div in divs:
        all_houses.append({
            "description": div.find("h2", class_="propertyCard-title").text,
            "price": div.find("div", class_="propertyCard-priceValue").text

        })

    return all_houses


def write_csv(all_houses):
    with open("rightmoveData.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(["test", "testing2", "testing3"])
    return "Done"


def main():
    url = ("https://www.rightmove.co.uk/property-for-sale/find.html?searchType"
           "=SALE&locationIdentifier=REGION%5E85310&insId=1&radius=0.0&min"
           "Price=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType="
           "&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primary"
           "DisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayProp"
           "ertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false")
    webpage = get_page(url)
    houses_list = get_data(webpage)
    write_csv(houses_list)


if __name__ == "__main__":
    main()
    print("Testing")
