class Solution:
    def sort012(self,arr,n):
        i, m, j = 0, 0, n-1
        while m<=j:
            if arr[m] == 0:
                arr[i], arr[m] = arr[m], arr[i]
                i, m = i+1, m+1
            elif arr[m] == 1:
                m += 1
            else:
                arr[m], arr[j] = arr[j], arr[m]
                j -= 1
            if arr[j] == 2:
                j -= 1