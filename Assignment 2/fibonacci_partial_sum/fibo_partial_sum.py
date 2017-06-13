# Uses python3
import sys
def get_fibonacci_arr(n):
    arr=[0,1,1];
    for i in range(3,n+1):
        arr.append((arr[i-1]+arr[i-2])%10)
    return arr

def fibonacci_partial(from_, to):
    sum=0
    arr=get_fibonacci_arr(to)
    for i in range(from_,to+1):
        sum+=arr[i]
    return sum%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial(from_, to))