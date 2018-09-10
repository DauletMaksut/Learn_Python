#Working with json, serilize and deserialize
import json
data = '''{
    "name" : "daulet",
    "phone": {
        "type": "laz",
        "number": "8 747 626 97 49"
        },
    "email": {
        "hide" : "yes"
        }
    }'''
info = json.loads(data)
print("Name is:", info["name"])
print("Hide it:", info["email"]["hide"])
