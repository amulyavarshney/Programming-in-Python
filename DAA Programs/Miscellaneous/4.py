# It returns true if there are any duplicate elements in the array else returns false.

def check(A, n):

	# Sort the array elements
    A.sort()

    for i in range(n-1):
        if A[i] == A[i+1]:
            print("The duplicate element is ",A[i])
            return True
    return False

# Driver program to test above function
if __name__ == "__main__":
    A = list(map(int, input("Enter the array elements : ").split()))
    if check(A, len(A)):
        print("The array have duplicated elements.")
    else:
        print("The array does not have duplicated elements.")

    print("The worst case time complexity is O(nlogn).")