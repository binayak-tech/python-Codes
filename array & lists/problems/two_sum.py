# write a program to find all pairs of integers whose sum is equal to a given number.
# There is only one pair exist in the array that sum up to the target value and you can't repeat the same index.


# Using hash map, time complexity is O(n)
def two_sum(arr,target):
    prevMap = {} # val : index

    for i, n in enumerate(arr):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i


# Brute force technique, T = O(n^2)
def two_sum_bruteforce(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]


arr = [2,7,11,15]

print(two_sum(arr,9))