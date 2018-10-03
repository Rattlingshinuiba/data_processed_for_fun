import csv
from matplotlib import pyplot as pl

class Myclass():
	x = 5
ABC = Myclass() # this is an object/ object is data which can be processed 

print('this is a random object in memory somewhere: ')
print(ABC)	
 
file_ = 'List of countries by population (United Nations) - Wikipedia - List of countries by population (United Nations) - Wikipedia.csv'

with open(file_) as f_object:
	lists = csv.reader(f_object) # returns an object
	
	print(lists) # prove it!
	
	header_row = next(lists)	# returns the first line of this file as a list
	
	print(header_row) # prove it!
	
	print(enumerate(header_row)) # returns an object
	for index, column_header in enumerate(header_row):
		print(index, column_header) # helpful in that subscripts r obvious
	
	pop_having_comma = []
	country_list = []
	pop_data = []
	
	
	for row in lists:
		pop_having_comma.append(row[3])
		country_list.append(row[1])
		
	
	
	for number in pop_having_comma:  # empty string inside?	
		
		'''>>> string = '82,000,00'
		>>> int(price_result.replace(',', ''))
		8200000'''
		
		pop_data.append(int(number.replace(',', '')))
		
	print(pop_data[0:10])		# comma is deleted
	
	
	
	
	colors = ['green', 'red', 'yellow', 'blue']
	exploded_style = [0.1, 0, 0, 0]  # world wedge separated from the rest
	pop = pop_data[0:4] # a example of 3 countries plus the world
	country = country_list[0:4]
	
	pl.pie(pop, explode=exploded_style, labels=country, colors=colors, autopct='%1.1f%%') # the first parameter is a positional one, so x is unnecessary
	pl.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
	pl.show()

	
	

