# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    print(data)
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    print(values)
    weights = data[3:(2 * n + 2):2]
    print(weights)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
