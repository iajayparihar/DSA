class BinarySearch:
    def Bsearch(self, key, arr, l, r):
        if l > r:
            return -1

        mid = l + (r-l)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return self.Bsearch(key, arr, l, mid-1)
        else:
            return self.Bsearch(key, arr, mid+1, r)


arr = [1, 2, 3, 4, 5, 6]
key = 3
a=BinarySearch().Bsearch(key, arr, 0, len(arr)-1)
print(a)
