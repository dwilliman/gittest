cars = 100 #here i am setting a variable to say that when i use cars it will put 100
space_in_car = 4.0 # here i am setting variable to be 4
drivers = 30 # as above but for 30
passengers = 90 # as above but for 90
cars_not_driven = cars - drivers # this should be 70 since cars 100 and drivers 30
cars_driven = drivers # here i am saying cars driven is equal to drivers variable which I set to 30 on line
carpool_capacity = cars_driven * space_in_car # 30 (as we are saying drivers , 30, times 4 so 120
average_passengers_per_car = passengers / cars_driven # 90 divided by 30, so 3


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
