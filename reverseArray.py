def reverseArray(arr):
    start, end = 0, len(arr)
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start +=1 
        end -= 1
    return arr
    
    
def reverseList(arr):
    rev = arr[::-1]
    return rev


def reverseArrayRecursive(arr, start, end):
    if start >= end: return
    arr[start], arr[end] = arr[end], arr[start]
    reverseArrayRecursive(arr,start+1, end-1)
    
    
    
A = [1, 2, 3, 4, 5, 6]
print(A)
print(f"Reversed list is: {reverseList(A)}")
