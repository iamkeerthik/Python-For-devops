
#import helper
#import helper as h
#from helper import *
# import os
# print(os.name)
from helper import verify, user_input_message
inputs= ""
while inputs != "exit":   #While loop
    inputs=input(user_input_message)
    days_and_units=inputs.split(":")
    days_and_units_dictionary= {"days": days_and_units[0], "unit":days_and_units[1]}
    print(days_and_units_dictionary)
    #helper.verify(days_and_units_dictionary)
    #h.verify(days_and_units_dictionary)
    verify(days_and_units_dictionary) 

