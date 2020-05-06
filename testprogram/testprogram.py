#!/usr/bin/env python3

print ("Musical recommendation based on emotion") 

feeling = Input("how are you feeling today")
if feeling.lower()== "sad":
    print ("listen to some blues")
else: 
    print ("you did not answer")
