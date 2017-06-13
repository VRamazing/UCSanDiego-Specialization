# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    else:
        arr=[0,1];
        sum=1
        for i in range(2,n+1):
            arr.append((arr[i-1]+arr[i-2])%10)
            sum+=arr[len(arr)-1]
        return sum%10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
