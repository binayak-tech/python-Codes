def chocolateDistribution(arr, n, size):
    # n = number of students
    # size = length of array
    if (n == 0 or size == 0): return 0
    if (n > size): return -1
    
    #sorting the array
    arr.sort()
    
    # getting the maximum difference possible
    minDiff = arr[-1] - arr[0]
    
    for i in range(size - n + 1):
        minDiff = min(minDiff,  arr[i + n - 1] - arr[i])
        
    return minDiff
    
arr = [3, 4, 1, 9, 56, 7, 9, 12]
size = len(arr)
students = 5
print(chocolateDistribution(arr, students, size))
