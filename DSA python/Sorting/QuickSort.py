
def quick(A,s,e):
    start=s
    end=e
    pivote=A[start]
    while start<end:
        while (A[start]<=pivote):
            start=start+1
        while (A[end]>pivote):
            end=end-1
        if start<end:
            A[start],A[end]=A[end],A[start]
    if A[start]<pivote:
        A[start],A[e]=A[e],A[start]
    return end
def QuickSort(A,l,r):
    if l<r:
        loc=quick(A,l,r)
        QuickSort(A,l,loc-1)
        QuickSort(A,loc+1, r)

A=[5,4,3,2,1]
QuickSort(A, 0, len(A)-1)
print(A)

