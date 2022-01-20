# It returns the element which appears maximum number of times in the array.

def check(arr):
    n = len(arr)
    
	# Sort the array elements
    arr.sort()

    # find the max frequency using linear traversal
    max_count = 1; res = arr[0]; curr_count = 1
     
    for i in range(1, n):
        if (arr[i] == arr[i - 1]):
            curr_count += 1
             
        else :
            if (curr_count > max_count):
                max_count = curr_count
                res = arr[i - 1]
             
            curr_count = 1
     
    # If last element is most frequent
    if (curr_count > max_count):
     
        max_count = curr_count
        res = arr[n - 1]
     
    return res

# Driver program to test above function
if __name__ == "__main__":
    A = list(map(int, input("Enter the array elements : ").split()))
    print("The lement which appears maximum number of times in the array =", check(A))

    print("The worst case time complexity is O(nlogn).")