import requests
import os
import json

from geopy import distance
from dotenv import load_dotenv


def coffee_all():
    with open("coffee.json", "r", encoding="CP1251") as my_file:
        coffee_json = my_file.read()
    coffee = json.loads(coffee_json)
    index = 0
    for i in coffee:
        result = coffee[index]['Name'], coffee[0]['geoData']['coordinates'][0], coffee[0]['geoData']['coordinates'][1]
        index = index + 1
        return result


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lat, lon


def main():
    load_dotenv()
    apikey = os.getenv("KEY_YANDEX")
    address = input("Где вы находитесь ? ")
    point_1 = address
    point_2 = coffee_all
    coord_point_1 = fetch_coordinates(apikey, point_1)
    coord_point_2 = fetch_coordinates(apikey, point_2)
    print("Ваши координаты: ", coord_point_1)
    print("Расстояние :", str(distance.distance(coord_point_1, coord_point_2).km))


if __name__ == '__main__':
    main()
