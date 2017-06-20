#Uses python3

import sys

# Problem Introduction
# You have n ads to place on a popular Internet page. For each ad, you know how
# much is the advertiser willing to pay for one click on this ad. You have set up n
# slots on your page and estimated the expected number of clicks per day for each
# slot. Now, your goal is to distribute the ads among the slots to maximize the
# total revenue.


# Task. Given two sequences a 1 , a 2 , . . . , a n (a i is the profit per click of the i-th ad) and b 1 , b 2 , . . . , b n (b i is
# the average number of clicks per day of the i-th slot), we need to partition them into n pairs (a i , b j )
# such that the sum of their products is maximized.
# Input Format. The first line contains an integer n, the second one contains a sequence of integers
# a 1 , a 2 , . . . , a n , the third one contains a sequence of integers b 1 , b 2 , . . . , b n .
# Constraints. 1 ≤ n ≤ 10 3 ; −10 5 ≤ a i , b i ≤ 10 5 for all 1 ≤ i ≤ n.


def max_dot_product(a, b):
    #write your code here
    # print("A,B %s %s" % (a,b)) 
    res = 0
    # for i in range(len(a)):
    #     res += a[i] * b[i]

    if len(a)<=1:
        res += a[0] * b[0]
        return res
    else:
        a.sort()
        b.sort()
        for i in range(len(a)):
            res += a[i]*b[i]
        return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
