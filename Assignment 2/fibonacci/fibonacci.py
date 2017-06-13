# Uses python3
# Task. Given an integer n, find the nth Fibonacci number F n .
# Input Format. The input consists of a single integer n.
# Constraints. 0 ≤ n ≤ 45.
def calc_fib(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		arr=[1,1]
		for i in range(2,n):
			arr.append(arr[i-1]+arr[i-2])
		return arr[n-1]

n = int(input())
print(calc_fib(n))
