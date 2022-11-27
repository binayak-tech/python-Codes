from array import *

# 1. create an array and traverse -----
print("Solution 1")
my_arr = array('i', [1,2,3,8,10])

for i in my_arr:
    print(i, end=" ")

print()



# 2. access individual elements through indexes -----
print("Solution 2")
sum = 0
for i in range(len(my_arr)):
    sum += my_arr[i]
print(sum)




# 3. append values to the array using append() method -----
print("Solution 3")
my_arr.append(13)
print(my_arr)



# 4. insert value in an array using insert() method -------
print("Solution 4")
my_arr.insert(3,22)
print(my_arr)



# 5. Extend python array using extend() method ------
print("Solution 5")
arr = array('i', [22, 33])
my_arr.extend(arr)
print(my_arr)



# 6. Add items from list into array using fromlist() method ----
print("Solution 6")
new_list = [12, 13]
my_arr.fromlist(new_list)
print(my_arr)



# 7. Remove an array element using remove() method ----
print("Solution 7")
my_arr.remove(22)
print(my_arr)



# 8. Remove last element using pop() method ------
print("Solution 8")
my_arr.pop()
print(my_arr)



# 9. Fetch any element through its index using index() method ----
print("Solution 9")
print(my_arr.index(22))



# 10. Reverse a python array using reverse() method ------
print("Solution 10")
my_arr.reverse()
print(my_arr)



# 11. Get array buffer information through buffer_info() method ------
print("Solution 11")
print(my_arr.buffer_info())



# 12. Check for number of occurances of an element using count() method -------
print("Solution 12")
print(my_arr.count(13))


# 13. Convert array to python list with same element using tolist() method ------
print("Solution 13")
print(my_arr.tolist())



# 14 Slice elements from an array -----
print("Solution 14")
print(my_arr[1:4])