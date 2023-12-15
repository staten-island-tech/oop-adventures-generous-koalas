import random
import time
from hero import Hero
from Zombies import Enemy
from poopy import Fight

def main():
    Maroon=Hero(name="Maroon",health=200, damage=15,coins=20)
    zombies= [Enemy(name="Zombie",health=200,damage=10,reward=25)]
    Fight()