# Uses python3
import sys
# Task. Given two integers a and b, find their least common multiple.
# Input Format. The two integers a and b are given in the same line separated by space.
# Constraints. 1 ≤ a, b ≤ 2 * 10 9 .
# Output Format. Output the least common multiple of a and b.

#lcm is product of number divided by gcd Hence
def gcd(a, b):
    if b==0:
    	return a
    return gcd(b,a%b)

def lcm(a, b):
	return a*b//gcd(a,b)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
   
