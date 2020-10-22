#Defining Size of the Matrices, as well as the last number in the matrix
size = 501**2
#Only odd numbers fall on the diagonals so we only need to worry about the odd numbers in the matrices
oddnumbers_list = range(1,size+1,2)
#After the first four numbers we need to begin skipping over indexes in our list
skipper = 1
#We need an iterator to loop through the index since we aren't adding all the numbers in the list
i = 0
#This will obviously be our answer
sum = 1

#While loop will will iterate through list until we reach last number
while oddnumbers_list[i] != size:
	# a nested four loop is needed because we need to increase the number of indexes we have to skip after every four numbers are added
	for x in range(4):
		i+= skipper
		sum += oddnumbers_list[i]
	skipper += 1

#Self-explanatory :)
print(sum)
