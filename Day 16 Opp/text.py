def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print(fib(10))
n = int(input("Enter a number: "))
fib(n)
