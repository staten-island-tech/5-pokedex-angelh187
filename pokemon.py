import json

pokedex = open("./pokedex.json", encoding="utf8")
type = open("./types.json", encoding="utf8")
data = json.load(pokedex)
types = json.load(type)
 
""" for index, item in enumerate("./pokedex.json"):
    print("Item#: ",index) 
    print(item["name"]) """

lang = (input("Please select a language: "))
for item in types:
    print(item[lang])

element = (input("What element of pokemon do you want? "))
for item in data:
    if item["type"] == element: 
       print(item["name"]) 

       print("hi rat here")