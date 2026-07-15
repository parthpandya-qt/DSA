def sumUpperLower(matrix):
    upper_sum = 0
    lower_sum = 0
    n = len(matrix)
    
    for i in range(n):
        for j in range(n):
            if j > i:  # Upper triangular part
                upper_sum += matrix[i][j]
            elif j < i:  # Lower triangular part
                lower_sum += matrix[i][j]
    
    return upper_sum, lower_sum