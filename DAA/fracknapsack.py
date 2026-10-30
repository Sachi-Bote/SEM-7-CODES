
import time

def fractional_knapsack(weights, profits, capacity):
    items = []

    # Calculate profit-to-weight ratio
    for i in range(len(weights)):
        ratio = profits[i] / weights[i]
        items.append([ratio, weights[i], profits[i]])

    # Sort by highest ratio
    items.sort(reverse=True)

    total_profit = 0

    # Select items greedily
    for ratio, weight, profit in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_profit += profit
            capacity -= weight
        else:
            total_profit += ratio * capacity
            capacity = 0

    return total_profit


# Main program
n = int(input("Enter number of items: "))
weights = list(map(int, input("Enter weights: ").split()))
profits = list(map(int, input("Enter profits: ").split()))
capacity = int(input("Enter capacity: "))

if (n <= 0 or len(weights) != n or len(profits) != n
        or any(w <= 0 for w in weights)
        or any(p < 0 for p in profits) or capacity < 0):
    print("Invalid input")

else:
    start = time.perf_counter()

    result = fractional_knapsack(weights, profits, capacity)

    end = time.perf_counter()

    print("Maximum profit:", result)
    print("Execution time:", end - start, "seconds")
