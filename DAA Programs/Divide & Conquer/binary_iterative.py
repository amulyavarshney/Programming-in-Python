# Python 3 program for recursive binary search. 
# Returns index of key in array if present, else -1

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
    
def main():
    a = list(map(int, input("Enter the sorted array : ").split()))
    k = int(input("Enter the key : "))
    x = binary_search(a, k)
 
    if x != -1:
        print(f"{k} is present in the array at index = {x}.")
    else:
        print(f"{k} is not present in the array.")

if __name__ == "__main__":
    main()
    print("The worst case time complexity of Iterative Binary Search is O(logn).")
