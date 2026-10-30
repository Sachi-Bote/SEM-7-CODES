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