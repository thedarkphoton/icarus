import xml.etree.ElementTree as ElementTree

from os import walk
import re

data_folder = "extracted/"

def create_json(regexp, indicators):
    f = []
    for (dirpath, dirnames, filenames) in walk(data_folder):
        for file in filenames:
            if regexp.search(file):
                f += [file]
        break

    json = []
    for path in f:
        data = ElementTree.parse(data_folder + path).getroot()
        cars_json = {}
        for car in indicators:
            cars_json[car[0]] = data.find(car[1]).text

        json += [cars_json]

    return json

regexp = re.compile(r'\w+.capdata.xml')
test = create_json(regexp, [
    ["price", "./data/cap_data/new_prices/price/basic_price"]
])

print(test)