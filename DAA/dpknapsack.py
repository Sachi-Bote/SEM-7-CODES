"""import time

def knapsack(weights, profits, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]

            if weights[i - 1] <= w:
                value = profits[i - 1] + dp[i - 1][w - weights[i - 1]]

                if value > dp[i][w]:
                    dp[i][w] = value

    return dp[n][capacity]


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
    result = knapsack(weights, profits, capacity)
    end = time.perf_counter()

    print("Maximum profit:", result)
    print("0/1 Knapsack execution time:",
          end - start, "seconds")
"""

import time

def knapsack(weights, profits, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]

            if weights[i - 1] <= w:
                value = profits[i - 1] + dp[i - 1][w - weights[i - 1]]

                if value > dp[i][w]:
                    dp[i][w] = value

    # Print DP Table
    print("\nDP Table:")
    print(f"{'Items/Capacity':<16}", end="")

    for w in range(capacity + 1):
        print(f"{w:<8}", end="")

    print()

    for i in range(n + 1):
        if i == 0:
            label = "No Item"
        else:
            label = "Item " + str(i)

        print(f"{label:<16}", end="")

        for w in range(capacity + 1):
            print(f"{dp[i][w]:<8}", end="")

        print()

    # Find selected items
    w = capacity
    selected = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i)
            w = w - weights[i - 1]

    return dp[n][capacity], selected


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

    result, selected = knapsack(weights, profits, capacity)

    end = time.perf_counter()

    print("\nMaximum profit:", result)

    print("Selected items:")
    for i in selected:
        print("Item", i, "- Weight:", weights[i - 1],
              "Profit:", profits[i - 1])

    print("0/1 Knapsack execution time:",
          end - start, "seconds")
