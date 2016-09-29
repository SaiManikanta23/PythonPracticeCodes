searchfile = open("output.txt", "r")
for line in searchfile:
    if ('t') in line: print line,
searchfile.close()

