class Solution:
    def squaresInChessBoard(self, N):
        return sum([i*i for i in range(1, N+1)])

#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.squaresInChessBoard(N))