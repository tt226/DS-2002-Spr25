#!/usr/bin/env python3


import os 

user_name = input("Type your name? ")
user_food = input("Type your favorite food? ")
user_game = input("Type your favorite game? ")
user_drink = input("What's your favorite drink? ")

os.environ['YOUR_NAME'] = user_name
os.environ['FAV_FOOD'] = user_food
os.environ['FAV_GAME'] = user_game
os.environ['FAV_DRINK'] = user_drink


user_name = os.getenv('YOUR_NAME')
favorite_food = os.getenv('FAV_FOOD')
favorite_game = os.getenv('FAV_GAME')
favorite_drink = os.getenv('FAV_DRINK')


print(f"{user_name}'s favorite food is {favorite_food}.")
print(f"{user_name}'s favorite game is {favorite_game}.")
print(f"{user_name}'s favorite drink is {favorite_drink}.")

