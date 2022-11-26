def containsDuplicates(arr):
  
  # set can only contain distinct elements,
  # when we add the list to set it deletes all duplicate elements therefore if there is any duplicate then the size of the set will decrease.
  return len(set(arr)) != len(arr)

arr = [1, 2, 3, 1]
print(containsDuplicates(arr))
