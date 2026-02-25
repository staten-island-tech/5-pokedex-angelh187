import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)

for index, item in enumerate("./pokedex.json"):
    print("Item#: ",index) 
    print(item["name"])