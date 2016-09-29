with open('output.txt', 'w') as f:
    f.write('Hello World! Welcome to python programming')
#Opening an output file and writing above line in it
fo = open("output.txt", "r+")
str = fo.read(10);
print "String is : ", str

# Check current position in the file
position = fo.tell();
print "file position is : ", position

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10);
print "Again String is : ", str
# Close opend file
fo.close()
