def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  # turn the set into a list (as requested)
  return list( seen_twice )
#Input Sequence
seq = [1,1,2,2,3,4,6,7]
#Calling the function to list all duplicates
list_duplicates(seq)
print (list_duplicates(seq))
