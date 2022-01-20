# Dynamic programming using memorization

import sys
dp = [[-1 for i in range(100)] for j in range(100)]

# Function for matrix chain multiplication
def matrixChain(p, i, j):
	if(i == j):
		return 0
	
	if(dp[i][j] != -1):
		return dp[i][j]
	
	dp[i][j] = sys.maxsize
	
	for k in range(i,j):
		dp[i][j] = min(dp[i][j], matrixChain(p, i, k) + matrixChain(p, k + 1, j)+ p[i - 1] * p[k] * p[j])
	
	return dp[i][j]

def MatrixChainOrder(p,n):
	i = 1
	j = n - 1
	return matrixChain(p, i, j)

# Driver Code
if __name__ == "__main__":
    A = list(map(int, input("Enter the array elements : ").split()))
    print("Minimum number of multiplications is",MatrixChainOrder(A, len(A)))

    print("The worst case time complexity is O(n*n*n).")