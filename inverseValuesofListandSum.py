string_input = raw_input()
input_list = string_input.split() #splits the input string on spaces
# process string elements in the list and make them integers
myList = [int(a) for a in input_list]
print (myList)
myInt = 10.0
newList = [myInt / x for x in myList]
myList[:] = [myInt / x  for x in myList]
sumx=sum(newList)
print (sumx)
