#!/usr/bin/env python3
col_list= ["blue", "columbus"]
col_list.append("1942")
print ("what is your name?") # gotta have quotes around strings
user_input= input() # this line is good!

# Looks like you're starting an f-string. I'll make a correct version and you can compare.

# print In (col_list[2]),(col_list[1]) sailed the ocean(col_list[0],(user_input) fell off the boat

print(f"In {col_list[2]}, {col_list[1]} sailed the ocean {col_list[0]}. {user_input} fell off the boat.") # <-- was missing the end parenthesis!! My bad.
