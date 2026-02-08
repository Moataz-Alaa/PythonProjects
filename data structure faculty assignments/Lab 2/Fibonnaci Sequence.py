

def fibonacci(n):
    fib_memory = [0,1]
    if n == 1:
         return 0
    if n == 2:
         return 1
    for _ in range(n - 2):
            fib_n = fib_memory[0] + fib_memory[1]
            fib_memory[0] = fib_memory[1]
            fib_memory[1] = fib_n
    return fib_n

print(fibonacci(8))