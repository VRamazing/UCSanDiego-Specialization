# Uses python3
# Task. Given two integers a and b, find their greatest common divisor.
# Input Format. The two integers a, b are given in the same line separated by space.
# Constraints. 1 ≤ a, b ≤ 2 · 10 9 .
# Output Format. Output GCD(a, b).
import sys

def gcd(a, b):
    if b==0:
    	return a
    return gcd(b,a%b)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
