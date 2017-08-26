# Python Program for recursive binary search.

# Returns index of key in arr if present, else -1
def binarySearch(arr, low, high, key):
    # Check base case
    if high >= low:

        mid = low + (high - low) // 2

        # If element is present at the middle itself
        if arr[ mid ] == key:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[ mid ] > key:
            return binarySearch (arr, low, mid - 1, key)

        # Else the element can only be present in right subarray
        else:
            return binarySearch (arr, mid + 1, high, key)

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [ 2, 3, 4, 10, 40 ]
key = 1

# Function call
result = binarySearch (arr, 0, len (arr) - 1, key)

if result != -1:
    print ("Element is present at index %d" % result)
else:
    print ("Element is not present in array")
