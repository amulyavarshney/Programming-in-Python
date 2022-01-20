class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        m = arr[-1]+1
        i, j = 0, n-1
        for k in range(n):
            if k&1:
                arr[k] += (arr[i]%m)*m
                i += 1
            else:
                arr[k] += (arr[j]%m)*m
                j -= 1
        for k in range(n):
            arr[k] //= m