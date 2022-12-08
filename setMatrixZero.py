def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    rowZero = False
    
    # STAGE 1, HERE WE TRAVERSE THROUGH THE MATRIX AND SET FIRST ROW AND FIRST COLUMN TO ZEOR IF ANY ELEMENT OF THAT ROW OR COLOUMN HAS 0.
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0

                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True
                    
    # STAGE 2, HERE WE CHECK IF THE FIRST ROW OR FIRST COLUMN HAS 0 THEN WE SET THE CURRENT ELEMENT TO ZERO
    # IN THIS PROCESS EVERY ELEMENT THAT IS REQURIRED TO BE ZERO IS SET TO ZERO EXCEPT THE FIRST ROW AND FIRST COLUMN
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

                
                
    # STAGE 3, HERE WE SET THE ENTIRE FIRST COLUMN TO 0 IF NEEDED
    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0
            
            

    # STAGE 4, HERE WE SET ENTIRE FIRST ROW TO 0 IF NEEDED
    if rowZero:
        for c in range(cols):
            matrix[0][c] = 0
            
            
            
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
newMatrix = setZeroes(matrix)
print(newMatrix)
