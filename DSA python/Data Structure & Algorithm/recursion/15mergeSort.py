def merge(arr, l, r,mid):
    len1 = mid - l + 1
    len2 = r - mid

    first = []
    second = []

# copy array in first and second
    mindex = l
    for i in range(len1):
        first.append(arr[mindex])
        mindex += 1

    for i in range(len2):
        second.append(arr[mindex])
        mindex += 1

# append value in the main Array
    index1 = index2 = 0 ; mindex = l
    while index1 < len1 and index2 < len2:
        if first[index1] < second[index2]:
            arr[mindex] = first[index1]
            index1 += 1
        else:
            arr[mindex] = second[index2]
            index2 += 1
        mindex += 1

    while index1 < len1:
        arr[mindex] = first[index1]
        index1 += 1
        mindex += 1

    while index2 < len2:
        arr[mindex] = second[index2]
        index2 += 1
        mindex += 1

    # print(arr)


def mergeSort(arr, l, r):
    if l >= r:
        return
    mid = l + (r-l)//2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid+1, r)

    merge(arr, l, r,mid)
    # print(arr,l,r,mid)


# Driver Code
if __name__ == '__main__':
    arr = [6, 5, 4, 3, 2, 1,0,77]
    print("Given array is", arr, end="\n")
    mergeSort(arr, 0, len(arr)-1)
    print("Sorted array is: ", arr, end="\n")
