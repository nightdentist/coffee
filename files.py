import json

with open("coffee.json", "r", encoding="CP1251") as my_file:
    coffee_json = my_file.read()

coffee = json.loads(coffee_json)
first_coffee = coffee[0]['Name'], coffee[0]['geoData']['coordinates'][0], coffee[0]['geoData']['coordinates'][1]

index = 0

for i in coffee:
    result = coffee[index]['Name'], coffee[0]['geoData']['coordinates'][0], coffee[0]['geoData']['coordinates'][1]
    index = index + 1
    print(result)
