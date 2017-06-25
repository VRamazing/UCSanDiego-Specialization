#!/usr/bin/python3 
# Uses python3
import sys

def get_majority_element(a,n):
    d={}
    for i in a:
        if d.get(i) == None:
            d[i] = 1
        else:
            d[i]=d[i] + 1

    count = 0
    for x in d.values():
        if x > n/2:
            count+=1

    return count    

         

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a,n))
