# It returns true if there is triplet with sum equal to k is present in the array. Also, prints the triplet.

def check(A, arr_size, sum):

	# Sort the elements
	A.sort()

	# Now fix the first element one by one and find the other two elements
	for i in range(0, arr_size-2):
		# To find the other two elements, start two index variables from two corners of the array and move them toward each other.

        # index of the first element in the remaining elements
		l = i + 1
		
		# index of the last element
		r = arr_size-1
		while (l < r):
		
			if( A[i] + A[l] + A[r] == sum):
				print(f"The given array has 3 elements which are {A[i]}, {A[l]}, {A[r]}.")
				return True
			
			elif (A[i] + A[l] + A[r] < sum):
				l += 1
			else: # A[i] + A[l] + A[r] > sum
				r -= 1

	# If we reach here, then no triplet was found
	return False

# Driver program to test above function
if __name__ == "__main__":
    A = list(map(int, input("Enter the array elements : ").split()))
    k = int(input("Enter K : "))
    # A = [1, 4, 45, 6, 10, 8]
    # sum = 22

    if not check(A, len(A), k):
        print("The given array doesn't have 3 elements with the given sum.")

    print("The worst case time complexity is O(n*n).")
