def Merge(A, left, mid, right):
    b = [0, 0, 0, 0, 0, 0]
    i = left
    j = mid+1
    k = left
    while i <= mid and j <= right:
        if A[i] < A[j]:
            b[k] = A[i]
            i += 1
            k += 1
        else:
            b[k] = A[j]
            j += 1
            k += 1
    while j <= right:
        b[k] = A[j]
        k += 1
        j += 1
    while i <= mid:
        b[k] = A[i]
        k += 1
        i += 1
    print('b Array', b)


def MergeSort(A, left, right):
    if left < right:
        mid = (left+right)//2
        MergeSort(A, left, mid)
        MergeSort(A, mid+1, right)
        Merge(A, left, mid, right)


A = [1, 12, 5, 7, 8, 3]
length = len(A)
MergeSort(A, 0, length-1)
