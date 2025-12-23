def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)


n = 5
print(f'A szamok osszege 1-tol {n}-ig: {sum_recursive(n)}')

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
