
import time

# Recursive method
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Non-recursive method
def fib_iterative(n):
    a, b = 0, 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result


n = int(input("Enter number of terms: "))

if n < 0:
    print("Enter a non-negative number")
else:
    # Measure recursive method
    start = time.perf_counter()
    recursive_result = [fib_recursive(i) for i in range(n)]
    end = time.perf_counter()

    print("Recursive Fibonacci:", *recursive_result)
    print("Recursive execution time:", end - start, "seconds")

    # Measure non-recursive method
    start = time.perf_counter()
    iterative_result = fib_iterative(n)
    end = time.perf_counter()

    print("Non-recursive Fibonacci:", *iterative_result)
    print("Non-recursive execution time:", end - start, "seconds")
