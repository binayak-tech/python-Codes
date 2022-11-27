# METHOD 1
def find(num):
    assert int(num) == num and num >= 0, "Provide a positive integer only!"
    if num == 0:
        return 0
    return num % 2 + 10 * find(num//2)

# METHOD 2
def binary(num):
    if num == 0:
        return
    else:
        binary(num//2)
        print(num % 2, end="")

num = int(input())

print(find(num))
# binary(num)