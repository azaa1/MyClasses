#Task1
# Write a python program that prints out the number
# of minutes in seven weeks

print (7 * 7 * 24 * 60)


#Task2
# Write python code to print out how far light travels in centimeters
# in one nanosecond
# speed of light = 299 792 458 meters/second
# meter = 100 centimeters
# nanosecond = 1.0 / 1 000 000 000

print ((299792458 * 100) * (1/1000000000))

speed_of_light = 299792458
billionth = 1.0/1000000000
nanostick =  (speed_of_light * billionth * 100)
print (nanostick)


#Task3
# Given the variables defined here, write Python code that
# prints out the distance, in meters, that light travels in one
# processor cycle

#speed_of_light_1 in meters per second
#cycle_per_second is 2.7 GHz

speed_of_light_1 = 299792458.0
cycle_per_second = 2700000000.0

cycle_distance =  speed_of_light_1 / cycle_per_second
print (cycle_distance)


#Task4
# Write python code that defines the variable
# age to be your age in years, and then prints
# out the number of days you have been alive

age = 25
days_in_a_year = 365.25
age_in_days = age * days_in_a_year
print (age_in_days)
