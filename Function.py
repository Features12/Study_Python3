def a(i): #create new function
	i.append("blue") # add new element

b = ["red", "green"] #create list
a(b) # call function and add element of arguments function
print(b)
#Output:
#["red", "green", "blue"]