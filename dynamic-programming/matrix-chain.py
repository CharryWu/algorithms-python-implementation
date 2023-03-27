"""
Given the dimension of a sequence of matrices in an array arr[],
where the dimension of the ith matrix is (arr[i-1] * arr[i]),
the task is to find the most efficient way to multiply these matrices together
such that the total number of element multiplications is minimum.
"""
# Python program using memoization
# Function for matrix chain multiplication
def matrixChainMemoized(p, i, j, dp):
    if i == j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = float('inf')

    for k in range(i, j):
        curCount = p[i-1] * p[k] * p[j] # A*B, A.height = p[i-1], A.width = B.height = p[k], B.width = p[j]
        dp[i][j] = min(
            dp[i][j], matrixChainMemoized(p, i, k, dp) + curCount + matrixChainMemoized(p, k + 1, j, dp)
        )

    return dp[i][j]


def MatrixChainOrder(p, n):
    i = 1
    j = n - 1
    dp = [[-1 for __ in range(n)] for _ in range(n)]
    return matrixChainMemoized(p, i, j, dp)


# Driver Code
arr = [1, 2, 3, 4]
n = len(arr)
print("Minimum number of multiplications is", MatrixChainOrder(arr, n))

# This code is contributed by rag2127
