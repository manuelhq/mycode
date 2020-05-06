#!/usr/bin/env python3

#create dictionary

value = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"sp    eed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "inte    lligence": "average", "strength": "strongest"}}
#collect input
char_name = input("Which character do you want to know about? (Flash, Batman, Superman")
if char_name.lower()== "flash""batman""superman":
    print ("What statistic do you want to know about? (strength, speed, or intelligence")
char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence")
if char_stat.lower()== "strength""speed""inteligence":
    print(<char_name>'s <char_stat> is: <value>
    
