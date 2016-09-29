#!/usr/bin/py
def flipBits(a):
   return a ^ 4294967295 # 2^32 - 1
 
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(0,n):
        a = int(raw_input())
        res = flipBits(a)
        print res
