def maxSubarray(arr):
    max_so_far = arr[0]
    currSum = 0
    
    for num in arr:
        currSum += num
        if max_so_far < currSum: max_so_far = currSum
        if currSum < 0: currSum = 0
    
    return max_so_far
    
print(maxSubarray([-1,-2,-3,-4]))
