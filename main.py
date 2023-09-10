my_name = input("what is your name")
my_age =int(input("what is your age"))
print(f"my name is{my_name} and I am {my_age}years old")
First_number =int(input("enter the first number"))
second_number =int(input("enter the second number"))
operation =input("what is the operation? ")
if operation == '+':
    print(First_number + second_number)
elif operation=="-":
    print(First_number - second_number)
elif operation=="*":
    print(First_number * second_number)
elif operation=="/":
    print(First_number / second_number)
else :
    print("wrong")
bus_capacity=35
people_inbus=int(input("enter the number of people who want to enter the bus"))
waiting=int(input("how many people are waiting?"))
empty_seats= bus_capacity - people_inbus 
if empty_seats>=waiting :
    print("come join us")
    print(empty_seats)
else :       
    print("the bus is full")



