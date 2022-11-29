'''
Given an array arr[] of n integers,
construct a Product Array prod[] (of same size) such that prod[i] is equal to the product of all the elements of arr[] except arr[i].
Solve it without division operator in O(n) time.
'''

'''
ALGORITHM 

1. create an output array of length n and assign each value to 1
2. create a prefix variable and set its value to 1
3. run a loop from 0 - n and update the output array by assigning the prefix value
suggesting that the value at res[i] will be multiplication of all the values in the given array before ith element,
4. after assigning the prefix value update the prefix each time by multipling it to the ith element in the given array.

5. create a postfix variable and set its value to 1
6. run a loop in reverse order from n-1 to 0 --> range(n-1,-1,-1)
7. uptate the output list by multiplying ith element with postfix element, 
where postfix element contains the multiplication value of all the element came after the ith element.

8. return the output array
'''



def productArray(nums):
    
    n = len(nums)
    res = [1]*n
    
    # storing the multiplication values before the ith element in the res list. res = [1,1,2,6] for input 1,2,3,4
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    
    # updating the res array by multiplying the multiplication values of all the elements after the current element, postfix = 1 -> 4 -> 12 -> 24 
    postfix = 1
    for i in range(n-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
        
    return res
    
    
# Driver code
arr = [1,2,3,4]
print("The product array is:")
print(productArray(arr))
