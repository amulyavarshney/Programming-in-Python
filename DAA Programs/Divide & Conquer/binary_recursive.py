# Python 3 program for recursive binary search. 
# Returns index of key in array if present, else -1

def binary_search(arr, left, right, key):
    if right >= left:

        # calculating the index of middle element
        mid = (right + left) // 2

        # if element at middle index is equal to key, then return the index.
        if arr[mid] == key:
            return mid

        # if element at middle index is greater than key, the element can be present at left side of middle element.
        elif arr[mid] > key:
            return binary_search(arr, left, mid - 1, key)

        # if element at middle index is less than key, the element can be present at right side of middle element.
        else:
            return binary_search(arr, mid + 1, right, key)
    
    # if key is not found in the array, return -1
    else:
        return -1
 
def main():
    a = list(map(int, input("Enter the sorted array : ").split()))
    k = int(input("Enter the key : "))
    x = binary_search(a, 0, len(a)-1, k)
 
    if x != -1:
        print(f"{k} is present in the array at index = {x}.")
    else:
        print(f"{k} is not present in the array.")

if __name__ == "__main__":
    main()
    print("The worst case time complexity of Recursive Binary Search is O(logn).")