# this program reads in a text file and performs mathematical functions: minimum, maximum and average

# import math to use the ceil function
import math

# defining the function to get a minimum value
def min(string):
# create a list from comma seperated numbers
	list = string.split(",")
# cast the numbers to int data types	
	numbers = [int(x) for x in list]
# sort the list from small to large	
	numbers.sort()
# return the first number, which will be the smallest	
	return numbers[0]

# defining the function to get the maximum value
def max(string):
# create a list from comma seperated values
	list = string.split(",")
# cast the numbers to int data type
	numbers = [int(x) for x in list]
# sort the numbers from small to large
	numbers.sort()
# return the last number which will be the largest
	return numbers[-1]

# defining a function to get the average
def avg(string):
# create a list from the comma seperated values	
	list = string.split(",")
# cast the numbers to int data type
	numbers = [int(x) for x in list]
# divide the sum by the count and return
	return sum(numbers) / len(numbers)

# defining a function to calculate percentile 
def percentile(number,string):
# create a list from the comma seperated values	
	list = string.split(",")
# cast the numbers to int data type
	numbers = [int(x) for x in list]
# sort the numbers
	numbers.sort()
# perform the calculation	
	return math.ceil(int(number)/100*len(list))

# create a dictnoary that will turn strings into callable functions
commands = {
	"min": min, 
	"max": max,
	"avg": avg
}
		
# open the file "input.txt"
with open("input.txt", "r", encoding="utf-8-sig") as input:

# split each line into a list containing a function and comma seperated numbers	
	for line in input:
		calculation = line.split(":")

# if the line starts with a "p" call the percentile function
# the 2 numbers before the ":" get assigned to the "number" parameter of the function
		if calculation[0][0] == "p":
			print(percentile(calculation[0][1:3], calculation[1]))

# if not, get the correct function from the dictionary, perform the calculation and print the output		
		else:					
			print(commands[calculation[0]](calculation[1]))