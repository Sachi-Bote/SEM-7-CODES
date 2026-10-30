
# Fractional Knapsack using Greedy Method

def fractional_knapsack(weights, profits, capacity):

    n = len(weights)

    # Calculate profit/weight ratio
    ratio = []

    for i in range(n):
        ratio.append(profits[i] / weights[i])

    # Sort items by ratio in descending order
    for i in range(n):
        for j in range(i+1, n):
            if ratio[i] < ratio[j]:
                ratio[i], ratio[j] = ratio[j], ratio[i]
                weights[i], weights[j] = weights[j], weights[i]
                profits[i], profits[j] = profits[j], profits[i]

    total_profit = 0

    print("\nSelected Items:")

    for i in range(n):

        if capacity == 0:
            break

        if weights[i] <= capacity:
            capacity -= weights[i]
            total_profit += profits[i]
            print("Item", i+1, "- Fully selected")

        else:
            fraction = capacity / weights[i]
            total_profit += profits[i] * fraction
            print("Item", i+1, "- Fraction selected:", round(fraction, 2))
            capacity = 0

    print("\nMaximum Profit:", round(total_profit, 2))


# User Input
n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    print("\nItem", i+1)
    weights.append(float(input("Enter weight: ")))
    profits.append(float(input("Enter profit: ")))

capacity = float(input("\nEnter knapsack capacity: "))

fractional_knapsack(weights, profits, capacity)
