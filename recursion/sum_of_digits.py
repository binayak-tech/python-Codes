def sum_of_digits(num):
    assert num >= 0 and int(num) == num, "Number must be a positive integer"

    if num == 0:
        return 0
    else:
        return num % 10 + sum_of_digits(num//10)

n = int(input())
print(sum_of_digits(n))