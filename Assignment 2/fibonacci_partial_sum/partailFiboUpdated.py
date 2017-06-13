# Uses python3
import sys
def get_fibonacci_arr(n):
    arr=[0,1,1];
    for i in range(3,n+1):
        arr.append((arr[i-1]+arr[i-2])%10)
        print arr
    return arr

def fibonacci_partial(from_, to):
    arr=get_fibonacci_arr(to)
    sum=arr[from_-2] + arr[to-1]

    for i in range(from_-1,to-1):
        sum+=2*arr[i]
    return sum%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial(from_, to))