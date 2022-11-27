# Find out if a given list has all unique elements or not.
# if unique return true else false
# using hashmap

def isUnique(arr):
    prev_map = {} # val: index

    for i, n in enumerate(arr):
        if n in prev_map:
            return False
        prev_map[n] = i
    return True

# arr = "ganesh"  
arr = [1,2,3,4,4]
print(isUnique(arr))