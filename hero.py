
import json
import os


class Dogs():
    def create (self):
     name= input("Enter name:")
     damage= input("Enter damage:")
     health= input("Enter health:")
     cla ={"name":name, "size":damage,  "color":health}
     return(cla)
        
