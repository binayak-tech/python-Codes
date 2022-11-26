def minMax(arr):
    n = len(arr)
    min, max = 0,0
    if n == 1:
        return arr[0], arr[0]
    elif n == 2:
        if arr[0] > arr[1]: 
            return arr[1], arr[0]
        else:
            return arr[0], arr[1]
    else:
        for i in arr:
            if i < min: min = i
            elif i > max: max = i
        return min, max
 
min, max = minMax([1,2,3,4,5,-2])
print(f"minimum = {min} and maximum = {max}")
