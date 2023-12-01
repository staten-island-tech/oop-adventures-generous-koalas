import json
import os

class Zombie():
    def create(self):
        name= input("Enter name: ")
        health= input("Enter health: ")
        damage= input("Enter damage: ")
        poop={"name":name, "health":health, "damage":damage}
        return(poop)


with open("data.json", "r") as f:
    data = json.load(f)

a= Zombie()
a1=a.create()
data.append(a1)

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data, indent=4)

    f.write(json_string)

os.remove("data.json")
os.rename(new_file, "data.json")
