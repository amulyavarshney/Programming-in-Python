# Python 3 program for implementation of QuickSort
# Returns the sorted array

def partition(arr,left,right):
	i = left+1
	j = right
	pivot = arr[left]
	while(i<=j):
		while(arr[i]<pivot and i<right):
			i = i+1
		while(arr[j]>pivot):
			j = j-1
		if(i<j):
			arr[i], arr[j] = arr[j], arr[i]
			i = i+1
			j = j-1
		else:
			i = i+1
	arr[left] = arr[j]
	arr[j] = pivot
	return j
 
def quickSort(arr,left,right):
	if left >= right:
		return
	pivot = partition(arr, left, right)
	quickSort(arr, left, pivot-1)
	quickSort(arr, pivot+1, right)

def main():
    a = list(map(int, input("Enter the unsorted array : ").split()))
    n = len(a)
    quickSort(a, 0, n-1)
    print("Sorted array : ", *a, sep=' ')

if __name__ == "__main__":
	main()
	print("The worst case time complexity of Quick Sort is O(n*n).")