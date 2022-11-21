def factorial(n):
    if n < 0 :
        raise ValueError
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(1))