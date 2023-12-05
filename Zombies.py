import json
import os

class Zombie():
    def __init__(self,name,health,damage):
        self.name=name
        self.health=health
        self.damage=damage
        lo={"name":name, "health":health, "damage":damage}
        return(lo)


with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)

a= Zombie()
a1=a.create()
data.append(a1)


# Creates a new JSON file with the updated
# data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data, indent=4)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")