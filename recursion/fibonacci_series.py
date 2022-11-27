def fibonacci_numbers(n):
    assert n >= 0 and int(n) == n, "Number must be a positive integer"

    if n in [0,1]:
        return n
    else:
        return fibonacci_numbers(n-1) + fibonacci_numbers(n-2)


num = int(input())
#TO PRINT ONE RESULT
print(fibonacci_numbers(num))


# TO PRINT SEQUENCE
for i in range(num):
    print(fibonacci_numbers(i), end = ' ')