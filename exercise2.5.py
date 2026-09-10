# Exercise 2.5
import math

numbers = input("Enter float numbers separated by spaces: ")
numbers = [float(x) for x in numbers.split()]

for number in numbers:
    sine_value = math.sin(number)
    print("sin(", number, ") =", sine_value)