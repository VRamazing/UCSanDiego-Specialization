# Uses python3
import sys

def get_change(m):
    coins = [1,5,10]
    counter = 0
    while m > 0:
        for i in range(2,-1,-1):
            while m-coins[i] > -1:
                m = m - coins[i]
                counter+=1
        
    return counter

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
