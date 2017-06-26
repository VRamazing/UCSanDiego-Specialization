# Uses python3
import sys

def sumList(a):
	sum=0
	for i in a:
		sum=sum+i
	return sum

def optimal_summands(n):
    summands = []
    #write your code here
   	   	#2 = 2  ------------------> n/2 ==1
    	#3 = 1 + 2 ---------------> n/2 >= 1
    	#4 = 1 + 3 ---------------> n/3 > 1
    	#5 = 1 + 4 ---------------> n/3 > 1
    	#6 = 1 + 2 + 3 -----------> n/4 > 1
    	#7 = 1 + 2 + 4 -----------> n/4 > 1
    	#8 = 1 + 2 + 5 -----------> n/4 > 1
    	#9 = 1 + 2 + 6 -----------> n/4 > 1
    	#10 = 1 + 2 + 3 + 4 -----------> n/5 > 1
    	#11 = 1 + 2 + 3 + 5	-----------> n/3 > 1
    	#12 = 1 + 2 + 3 + 6 -----------> n/3 > 1
    	#13 = 1 + 2 + 3 + 7 -----------> n/3 > 1
    	#14 = 1 + 2 + 3 + 8 -----------> n/3 > 1
    	#15 = 1 + 2 + 3 + 4 + 5 -----------> n/3 > 1 
    	#16 = 1 + 2 + 3 + 4 + 6 -----------> n/3 > 1
    	#17 = 1 + 2 + 3 + 4 + 7 -----------> n/3 > 1
    	#18 = 1 + 2 + 3 + 4 + 8 -----------> n/3 > 1
    	#19 = 1 + 2 + 3 + 4 + 9 -----------> n/3 > 1
    	#20 = 1 + 2 + 3 + 4 + 10 -----------> n/3 > 1
    	#21 = 1 + 2 + 3 + 4 + 5 + 6 -----------> n/3 > 1

    if n/2 <= 1:
    	summands.append(n)
    	break
    else:
    	summands.append(1)
    	r=n-1 #Current value of n.Left over elements to be broken down.
    	while(not sumList(summands) == n)





    

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
