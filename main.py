my_name = input("what is your name")
my_age =int(input("what is your age"))
print(f"my name is{my_name} and I am {my_age}years old")
First_number =int(input("enter the first number"))
second_number =int(input("enter the second number"))
operation =input("what is the operation? ")
if operation == '+':
    print("first number + second number")
elif operation=="_":
    print("first number _ second number")
elif operation=="*":
    print("first number * second number")
elif operation=="/":
    print("first number / second number")
else :
    print("wrong")
bus_capacity=input("enter the number of passengers")
people_inbus=input("enter the number of people who want to enter the bus")
waiting=input("how many people are waiting?")
empty_seats= bus_capacity - people_inbus 
if empty_seats>=waiting :
    print("come join us")
else :
    print("the bus is full")



