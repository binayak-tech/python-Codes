def searchMatrix(matrix,target):
    ROWS, COLS = len(matrix), len(matrix[0])
    left, right = 0,ROWS-1
    while left <= right:
        row = (left + right) // 2
        if target > matrix[row][-1]: left = row + 1
        elif target < matrix[row][0]: right = row - 1
        else: break

    if left > right:
        return False
    row = (left + right) // 2
    l, r = 0, COLS-1
    while l <= r:
        mid = (l + r) // 2
        if target > matrix[row][mid]: l = mid + 1
        elif target < matrix[row][mid]: r = mid - 1
        else: 
            return True
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

print(searchMatrix(matrix, 3))