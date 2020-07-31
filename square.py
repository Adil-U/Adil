from functions import square

for i in range (10):
	print(f"The square of {i} is {square(i)}")

#the second way
#import functions  
#for i in range (10):
#	print(f"The square of {i} is {functions.square(i)}")




#HOW TO SORT A DICT
people = [
	{"name":"Adil","Hobby":"Football"},
	{"name": "Dias", "Hobby":"CS:GO"},
	{"name": "Draco", "Hobby":"Run"}

]
def so(person):
	return person["Hobby"]
people.sort(key = so)

print(people)