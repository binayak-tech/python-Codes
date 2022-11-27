# find the missing element from an integer array of 1 to n.


def missing_number(arr, n):
    expected_sum = int(n * (n+1) / 2)
    actual_sum = sum(arr)
    print(f"The missing number is {expected_sum - actual_sum}")

arr = [1,2,3,4,5,7,8,9,10]
missing_number(arr, 10)