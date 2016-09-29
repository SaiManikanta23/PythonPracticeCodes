#Program to Print squares of numbers in the given range
def printDict():
	d=dict()
	print "Enter the range to display the squares"
	x=int(raw_input())
	for i in range(0,x+1):
		d[i]=i**2
	for (k,v) in d.items():	
		print v
		

printDict()
