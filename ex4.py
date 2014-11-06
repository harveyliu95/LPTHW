#assign the number of the cars
cars = 100
#assign available capacity in each car
space_in_a_car = 4.0
#assign number of the drivers
drivers = 30
#assign the total number of passengers
passengers = 90
#assign the number of cars not driven, which equals to the number of cars minus the number of drivers
cars_not_driven = cars - drivers
#assign the number of cars driven, which is the same as the number of drivers
cars_driven = drivers
#assign the total available capacity
carpool_capacity = cars_driven * space_in_a_car
#assign the average number of passengers needed to be carried by each car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpoll today."
print "We need to put about", average_passengers_per_car, "in each car."
