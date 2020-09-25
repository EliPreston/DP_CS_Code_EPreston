import requests
import json
from pprint import pprint

# Get Key
# This is a file not in my respository I don't want you to have it
file = open("../API_KEYS/fixerkey.txt", "r")

key = file.read()
resp = requests.get('http://data.fixer.io/api/latest?access_key='+key)


# Converts response to JSON
data = resp.json()

# pretty print the data (formats it in a readable way in terminal)
# pprint(data)

# print(data["date"])
# print(data["base"])
# print(data["rates"]["CAD"])

# for rate in data["rates"]:
# print(rate)
# print(data[key])

# print(data["base"] + " --> " + rate)


for key in data["rates"]:
    print("1 " + data["base"] + " --> " + key + ": ", data["rates"][key])
