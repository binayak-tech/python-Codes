# check if the given arrays or strings contains all same elemenets, example bin is permutation of nib or bni.


# time complexity is O(n logn)
def permutation(arr1, arr2):
    if len(arr1) != len(arr2): return False
    arr1.sort()
    arr2.sort()
    if arr1 == arr2:
        return True
    else: return False

