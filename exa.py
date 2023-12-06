import json 
import os 

class Movies(): 
    def create (self): 
        title = input("Type in a title of a movie of your choice ")
        genre = input ("What genre is it? ")
        actor = input ("Tell me one of the actors that play in it ")
        year = input ("Put in a specific year is was released ")
        films = {"title": title, "genre": genre, "actor": actor, "year": year} 
        return (films) 

with open ("data.json", "r") as f:
    data = json.load(f) 

x = Movies() 
x1 = x.create() 
data.append(x1) 


new_file = "updated.json" 
with open(new_file, "w") as f: 
    json_string = json.dumps(data,indent=4) 

    f.write(json_string) 

os.remove ("data.json")
os.rename(new_file, "data.json")



## IN THIS FILE YOU WILL ONLY READ FROM THE JSON DATA USING CLASSES
import json
# Open the JSON file of pokemon data
test = open("data.json", encoding="utf8")
# create variable "data" that represents the enitre pokedex list
data = json.load(test)


movie = input("What movie do you want to find? You can input a title ,genre ,actor ,year , choose one!!: ") 
z=0


for i in range (len(data)): 
    if movie in data[i]["title"]:
            print (data[i])  
            z=1
    elif movie in data [i]["genre"]: 
            print (data[i]) 
            z=1 
    elif movie in data [i]["actor"]:
        print (data[i])  
        z=1
    elif movie in data [i]["year"]: 
        print (data[i]) 
        z=1 

if z!=1:
     print ("Movie is not saved or doesn't exist")

