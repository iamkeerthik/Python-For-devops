
from datetime import datetime

user_input=input("Enter goal with deadline in \"goal:date.month.year\" format\n")
input_list=user_input.split(":")

goal=input_list[0]
deadline=input_list[1]

deadline_date=datetime.strptime(deadline, "%d.%m.%Y")
# print(type(D.datetime.strptime(deadline, "%d.%m.%Y")))
#calculate how many days from  now till deadline
today_date=today_date=datetime.today()

time_remaining=deadline_date - today_date
print(f'Time remaining for your goal {goal} is {time_remaining.days} days')
# print(f'Time remaining for your goal {goal} is {int(time_remaining.total_seconds() / 60 / 60)} hours')