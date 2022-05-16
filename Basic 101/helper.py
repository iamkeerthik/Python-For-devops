
def days_to_min(days,conversion_unit):
    if conversion_unit == "hours":

        hours=days * 24
        print (f'{days} days equals to {hours} {conversion_unit}')
    elif conversion_unit == "minutes":
        min= days * 24 * 60
        print(f'{days} days equals to {min} {conversion_unit}')
    else:
        return "Unsupported unit"

def verify(days_and_units_dictionary):
    #if days.isdigit():
    try:
        input_days=int(days_and_units_dictionary["days"])
        if input_days > 0:
            days_to_min(input_days,days_and_units_dictionary["unit"])
        elif input_days == 0:
            print ("You enetered 0") 
        else:
             print ("You enetered -ve number,Enter +ve number") 
    except ValueError:
        print("eneter valid numeric ")  
user_input_message= "enter no of days:conversion unit \n"