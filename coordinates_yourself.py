import folium
import requests
import os
import json

from pprint import pprint
from geopy import distance
from dotenv import load_dotenv


def get_nearest_coffee(distance_coffees):
    return distance_coffees['distance']


def coffee_all(coord_point_1):
    with open("coffee.json", "r", encoding="CP1251") as my_file:
        coffee_json = my_file.read()
    all_coffees = json.loads(coffee_json)
    list_coffees = []
    map = folium.Map(coord_point_1[::-1])
    folium.Marker(
        location=coord_point_1[::-1],
        tooltip="Click me!",
        popup="Timberline Lodge",
        icon=folium.Icon(color="red"),
    ).add_to(map)
    for coffee in all_coffees:
        name = coffee['Name']
        lon = coffee['geoData']['coordinates'][0]
        lat = coffee['geoData']['coordinates'][1]
        coord_point_2 = lon, lat
        dict_coffees = dict()
        dict_coffees['title'] = name
        dict_coffees['distance'] = str(distance.distance(coord_point_1, coord_point_2).km)
        dict_coffees['longitude'] = lon
        dict_coffees['latitude'] = lat
        list_coffees.append(dict_coffees)
    sorted_coffees_distanse = sorted(list_coffees, key=get_nearest_coffee)
    five_coffees = sorted_coffees_distanse[:5]
    pprint(five_coffees)
    for five_coffee in five_coffees:
        long = five_coffee['longitude']
        lati = five_coffee['latitude']
        coord_point_3 = long, lati
        folium.Marker(
            location=coord_point_3[::-1],
            tooltip="Click me!",
            popup="Timberline Lodge",
            icon=folium.Icon(color="green"),
        ).add_to(map)
    map.save("index.html")


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
    return lon, lat


def main():
    load_dotenv()
    apikey = os.getenv("KEY_YANDEX")
    address = input("Где вы находитесь ? ")
    point_1 = address
    coord_point_1 = fetch_coordinates(apikey, point_1)
    print("Ваши координаты: ", coord_point_1)
    coffee_all(coord_point_1)


if __name__ == '__main__':
    main()
