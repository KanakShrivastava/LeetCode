class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        rows_to_zero = set()
        columns_to_zero = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    columns_to_zero.add(j)

        for row in rows_to_zero:
            for j in range(n):
                matrix[row][j] = 0

        for col in columns_to_zero:
            for i in range(m):
                matrix[i][col] = 0