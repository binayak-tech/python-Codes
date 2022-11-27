# rotate the given matrix by 90 degrees. 
"""
[1,2,3]
[4,5,6]
[7,8,9]

will be 

[7,4,1]
[8,5,2]
[9,6,3]

"""


def matrix_rotation(mat):
    left, right = 0, len(mat) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            temp = mat[top][left + i]
            mat[top][left + i] = mat[bottom - i][left]
            mat[bottom -i][left] = mat[bottom][right - i]
            mat[bottom][right - i] = mat[top + i][right]
            mat[top + i][right] = temp
            left += 1
            right -= 1
    return mat

mat = [
[1,2,3],
[4,5,6],
[7,8,9]
]
new_mat = matrix_rotation(mat)

for i in new_mat:
    print(i, sep=" ", end="\n")