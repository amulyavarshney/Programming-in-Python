class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,a,d,n):
        m = 10**5
        for i in range(n):
            a[i] += (a[(i+d)%n]%m)*m
        for i in range(n):
            a[i] //= m