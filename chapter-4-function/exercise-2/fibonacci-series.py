def fibonacci_series(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b)
    else:
        print(a, b, end=" ")
        for i in range(n - 2):
            c = a + b
            print(c, end=" ")
            a = b
            b = c
n = int(input("Enter the number of terms in the Fibonacci series: "))
fibonacci_series(n)