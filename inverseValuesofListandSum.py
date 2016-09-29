# Take raw input values from user in the format as 1 2 3 4 etc
string_input = raw_input()
input_list = string_input.split() #splits the input string on spaces
# process string elements in the list and make them integers
myList = [int(a) for a in input_list]
# Printing the list just to check whether they are converted into list
print (myList)
myInt = 1.0
#Inverse the list, Remember we sre taking myInt values as 1, which is 1/ each value
newList = [myInt / x for x in myList]
myList[:] = [myInt / x  for x in myList]
#Sum all the inverse values in the list as follows
sumx=sum(newList)
print (sumx)
