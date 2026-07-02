class SS:
    def srt(self,arr,l,n):
        # base case
        if l == n-1:
            return 

        # logical part
        min=l     
        for i in range(l,n):
            if arr[i] < arr[min]:
                min=i
        arr[l],arr[min]=arr[min],arr[l]

        # Recursion call
        self.srt(arr, l+1, n)

arr=[2,4,5,3,1]
l=0
n=len(arr)
SS().srt(arr, l, n)
print(arr)
