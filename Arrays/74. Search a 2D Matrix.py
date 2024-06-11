# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

matrix = [[1, 3, 5, 7], 
          [10, 11, 16, 20], 
          [23, 30, 34, 60]]
target = 30

def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    i = 0
    
    while i < n: 
        if target in range(matrix[i][0], matrix[i][m-1] + 1): 
            
            left, right = 0, m - 1

            while left <= right:
                mid = left + (right - left) // 2

                if target == matrix[i][mid]: 
                    return True
                elif target < matrix[i][mid]: 
                    right = mid - 1
                else:
                    left = mid + 1

        i += 1

    return False

print(searchMatrix(matrix, target))