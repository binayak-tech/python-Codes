def twoSum(nums, target):
    prevMap = {}
    for i,n in enumerate(nums):
        if n in prevMap:
            return [prevMap[n], i]
        prevMap[target - n] = i
        
arr = [1,5,6,23,63,44,2]
print(twoSum(arr,24))
