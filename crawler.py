import xml.etree.ElementTree as ElementTree

from os import walk
import re

#inputs
data_folder = "data/"
prefix = "{http://schemas.datacontract.org/2004/07/AudaAPI.Models}"
claims = [
    ["parts", "./"+prefix+"DamageEstimate/"+prefix+"Calculation/"+prefix+"Calculation/"+prefix+"InvalidParts/"+prefix+"InvalidPart/"+prefix+"GuideNumber"],
    ["scrapped", "./"+prefix+"Authorisation/"+prefix+"AuthorisationStatus"]

]

# don't modify
def create_json(claim_indicators):
    f = []
    regexp = re.compile(r'\w+.assessment.xml')
    for (dirpath, dirnames, filenames) in walk(data_folder):
        for file in filenames:
            if regexp.search(file):
                f += [file[:file.index(".")]]
        break

    parts = []
    cars = []

    for path in f:
        car_json = {}

        data = ElementTree.parse(data_folder + path + ".assessment.xml").getroot()
        car_json[claims[1][0]] = data.find(claims[1][1]).text

        for part in data.findall(claims[0][1]):
            parts += [part.text]
            if part.text not in parts:
                parts.append(part.text)


        car_json[claims[0][0]] = parts

        if car_json["scrapped"] != None and car_json["parts"] != None and (car_json["scrapped"] == "TotalLoss" or car_json["scrapped"] == "Authorised"):
            cars += [car_json]

    return { "parts": parts, "cars": cars }

json_data = create_json(claims)

print(json_data["parts"])
print(json_data["cars"])