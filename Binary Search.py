def binarySearch(list, x):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = low + (high-low) // 2


        if x == mid:
            return mid

        elif x < mid:
            high = mid - 1

        else:
            low = mid + 1
    return -1

if __name__ == '__main__':
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    x = 6

    result = binarySearch(list, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")