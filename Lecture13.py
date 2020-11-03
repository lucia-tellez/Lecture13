#!/usr/bin/python3

my_file = open("data.csv")

for thisline in my_file:
	if thisline.startswith("Drosophila melanogaster"):
		print(thisline)
	elif thisline.startswith("Drosophila simulans"):	
		print(thisline)
	else:
		print("This gene is not melanogaster or simulans")


