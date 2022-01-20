# Python 3 program to check fixed point in an array using binary search.
# Returns indedx of FIxed Point or -1 if there is no Fixed Point

def binarySearch(arr, left, right):
    if right >= left:

        # calculating the index of middle element
        mid = (left + right)//2

    # if element at index is equal to its index, then return the index.
    if mid is arr[mid]:
        return mid

    # if element at middle index is less than its index, the element can be present at right side of middle element.
    if mid > arr[mid]:
        return binarySearch(arr, mid + 1, right)

    # if element at middle index is greater than its index, the element can be present at left side of middle element.
    else:
        return binarySearch(arr, left, mid -1)

    # if such element is not found in the array, return -1
    return -1
    
def main():
    a = list(map(int, input("Enter the sorted array : ").split()))
    n = len(a)
    x = binarySearch(a, 0, n-1)

    if x != -1:
        print(f"Fixed Point is present in the array at index = {x}.")
    else:
        print(f"Fixed Point is not present in the array.")

if __name__ == "__main__":
    main()
    print("The worst case time complexity is O(logn).")