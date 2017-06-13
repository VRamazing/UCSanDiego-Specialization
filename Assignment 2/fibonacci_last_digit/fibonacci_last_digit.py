# Uses python3
# Task. Given an integer n, find the last digit of the nth Fibonacci number F n (that is, F n mod 10).
# Input Format. The input consists of a single integer n.
# Constraints. 0 ≤ n ≤ 10 7 .
# Output Format. Output the last digit of F
import sys

def get_fibonacci_last_digit_naive(n):
    arr=[1,1];
    for i in range(2,n):
        arr.append((arr[i-1]+arr[i-2])%10)
    return arr[n-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
