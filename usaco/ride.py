"""
ID: rosikan1
LANG: PYTHON3
PROG: ride  
-------------------
Problem name: Your Ride is Here
Problem url: https://train.usaco.org/usacoprob2?a=T9Emht6iUjd&S=ride 
Author: Rohan Sikand
"""

import string 
import numpy

def main():
	file = open('inputs/ride.txt') 

	sum_list = []
	for line in file:
		line = line.strip()
		converted_sum = get_sum(line)
		sum_list.append(converted_sum)

	if sum_list[0] == sum_list[1]:
		print('GO')
	else:
		print('STAY')


def get_sum(line):
	# line is a string
	conv_dict = {} 

	# populate dictionary
	count = 1
	for char in string.ascii_uppercase:
		conv_dict[char] = count
		count += 1

	# get product 
	num_list = []
	for char in line:
		value = conv_dict[char] 

	product = numpy.prod(num_list)

	return product % 47


# boilerplate 
if __name__ == '__main__':
    main()