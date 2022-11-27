def factorial(num):
    assert num >= 0 and int(num) == num, "Enter positive integers only!"
    
    if num in [0,1]:
        return 1
    else:
        return num * factorial(num-1)

num = int(input())
print(factorial(num))