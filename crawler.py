import xml.etree.ElementTree as ElementTree

from os import walk
import re

#inputs
data_folder = "data/"
cars = [
    ["price", "./data/cap_data/new_prices/price/basic_price"]
]
claims = [
    ["claim_no", "./{http://schemas.datacontract.org/2004/07/AudaAPI.Models}AssessmentNumber"]
]

# don't modify
def create_json(car_indicators, claim_indicators):
    f = []
    regexp = re.compile(r'\w+.capdata.xml')
    for (dirpath, dirnames, filenames) in walk(data_folder):
        for file in filenames:
            if regexp.search(file):
                f += [file[:file.index(".")]]
        break

    cars = []
    for path in f:
        car_json = {}

        data = ElementTree.parse(data_folder + path + ".capdata.xml").getroot()
        for car in car_indicators:
            car_json[car[0]] = data.find(car[1]).text

        data = ElementTree.parse(data_folder + path + ".assessment.xml").getroot()
        for claim in claim_indicators:
            car_json[claim[0]] = data.find(claim[1]).text

        cars += [car_json]

    return cars

test = create_json(cars, claims)

print(test)