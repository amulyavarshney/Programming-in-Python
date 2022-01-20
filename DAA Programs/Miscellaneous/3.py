# It returns true if there is a pair with sum equal to k is present in the array A and B. Also, prints the pair.

def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    
    while right >= left:

        # finding the index of middle element
        mid = (left + right) // 2

        # if element at middle index is less than key, the element can be present at right side of middle element.
        if arr[mid] < key:
            left = mid + 1

        # if element at middle index is greater than key, the element can be present at left side of middle element.
        elif arr[mid] > key:
            right = mid - 1

        # if element at middle index is equal to key, then return the index.
        else:
            return mid

    # if key is not found in the array, return -1
    return -1

def check(A, B, n, k):

	# Sort the elements
    A.sort()
    B.sort()

	# Now fix the element in array A one by one and find the other element in array B.
    for i in range(n):
        if binary_search(B, k-A[i]) != -1:
            print("Such a pair exists.")
            print("The elements are ", A[i], k-A[i])
            break
        else:
            print("No such pair exists.")

# Driver program to test above function
if __name__ == "__main__":
    A = list(map(int, input("Enter elements for array A : ").split()))
    B = list(map(int, input("Enter elements for array B : ").split()))
    k = int(input("Enter K : "))
    check(A, B, len(A), k)

    print("The worst case time complexity is O(nlogn).")