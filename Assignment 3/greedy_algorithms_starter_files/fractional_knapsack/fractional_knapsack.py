# Uses python3
import sys

# Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.

# Input Format. The first line of the input contains the number n of items and the capacity W of a knapsack.

# The next n lines define the values and weights of the items. The i-th line contains integers v i and w i 
#—the value and the weight of i-th item, respectively.

# Constraints : 1 ≤ n ≤ 10 3 , 0 ≤ W ≤ 2 · 10 6 ; 0 ≤ v i ≤ 2 · 10 6 , 0 < w i ≤ 2 · 10 6 for all 1 ≤ i ≤ n. 
# All the numbers are integers.

# Output Format : Output the maximal value of fractions of items that fit into the knapsack. The absolute
# value of the difference between the answer of your program and the optimal value should be at most
# 10 −3 . To ensure this, output your answer with at least four digits after the decimal point (otherwise
# your answer, while being computed correctly, can turn out to be wrong because of rounding issues


def get_optimal_value(capacity, weights, values):

    value = 0.
    valDensity=[]

	# Frst Step calculate value density ie list containing ratio of weight per unit weight and sort it in ascending order.
    for i in range(len(weights)):
    	valDensity.append(values[i]/weights[i])

    backup=valDensity.copy() #Store Density in backup variable before sorting. 
    if len(weights) > 1:
    	valDensity.sort(reverse=True)
    

    #Second Step - Start from element of max value density and try to fit it whole in capacity and if it doesn't take a fraction of it.
    totalValue=0
    for i in valDensity:
    	index=backup.index(i)
    	weight=weights[index]
    	value=values[index]
    	if capacity//weight >= 1:
    		capacity -= weight 
    		totalValue += value 
    	else:
    		if capacity==0:
    			break
    		totalValue += value*capacity/weight
    		capacity = 0
    return totalValue


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:0.5f}".format(opt_value))
