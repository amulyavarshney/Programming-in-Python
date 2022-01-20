# Finding whether there are two elements in the array such that their sum is equal to given element K or not?

def check(A, arr_size, sum):
    # sort the array
    mergeSort(A, 0, arr_size-1)
    l = 0
    r = arr_size-1
     
    # traverse the array for the two elements
    while l<r:
        if (A[l] + A[r] == sum):
            return 1
        elif (A[l] + A[r] < sum):
            l += 1
        else:
            r -= 1
    return 0
 
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0 , n1):
        L[i] = arr[l + i]
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
  
    i = j = 0
    k = l
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
  
def mergeSort(arr,l,r):
    if l < r:
        m = (l+(r-1))//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
     
# Driver program to test above function
if __name__ == "__main__":
    A = list(map(int, input("Enter the array elements : ").split()))
    k = int(input("Enter K : "))
    # A = [1, 4, 45, 6, 10, -8]
    # n = 16
    if check(A, len(A), k):
        print("The given array has 2 elements with the given sum.")
    else:
        print("The given array doesn't have 2 elements with the given sum.")

    print("The worst case time complexity is O(nlogn).")