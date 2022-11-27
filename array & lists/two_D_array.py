import numpy as np

two_d_array = np.array([[1, 3, 5, 7], [2, 4, 6, 8], [4, 8, 16, 32]])

two_d_array = np.insert(two_d_array, 0, [[0,1,2]], axis=1)

def array_traversal(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end = " ")
        print()

array_traversal(two_d_array)