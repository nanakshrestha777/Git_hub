"""
Write a Python script that calculates the sum, average and population standard
deviation of 5 numbers stored in the variables a,b,c,d,e The formula to calculate the
standard deviation of a number can be found below. To ensure that your calculation is
correct, use the following 5 numbers 9, 8, 12, 33, 5 and assign then into the 5 variables
a, b, c, d, e. The population standard deviation should equal to 10.051865498503252.
The formula to calculate the population standard deviation:
Here's how to calculate population standard deviation:
Step 1: Calculate the mean of the data—this is μ in the formula.
Step 2: Subtract the mean from each data point, and then square the result to make it
positive.
Step 3: Add the squared deviations together.
Step 4: Divide the sum by the number of data points in the population. The result is
called the variance.
Step 5: Take the square root of the variance to get the standard deviation.
"""


import math

a,b,c,d,e = 9,8,12,33,5

the_sum = a+b+c+d+e

average = the_sum / 5

deviation = [a - average, b - average, c - average, d - average, e - average]

squared_deviation = [ x**2 for x in deviation]

squared_deviation_sum = sum(squared_deviation)

variance = squared_deviation_sum / 5

standard_deviation = math.sqrt(variance) # math.sqrt means importing squareroot 


print("Sum: ", the_sum)
print("Average: ", average)
print(" Standard Deviation: ", standard_deviation)
"""
Sum:  67
Average:  13.4
Standard Deviation:  10.051865498503252
"""