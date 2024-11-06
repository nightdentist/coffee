import requests
import os

from geopy import distance
from dotenv import load_dotenv


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
    #address = input("Где вы находитесь ? ")
    point_1 = input("Пункт А: ")
    point_2 = input("Пункт Б: ")
    coord_point_1 = fetch_coordinates(apikey, point_1)
    print(coord_point_1)
    coord_point_2 = fetch_coordinates(apikey, point_2)
    #print("Ваши координаты: ", fetch_coordinates(apikey, address))
    print("Расстояние: ", distance.distance(coord_point_1, coord_point_2).km)


if __name__ == '__main__':
    main()
