class QS:
    def partition(self, arr, l, r):
        # select fist as a pivot element 
        pivot = arr[l]
        cnt = 0
        # count all lessthen pivot element
        for i in range(l+1,len(arr)):
            if pivot > arr[i]:
                cnt += 1
        # pivot index place in main arr
        pindex = l+cnt

        arr[pindex],arr[l]=arr[l],arr[pindex]

        i=l # start
        j=r # end
        # lessthen < pivot > graterthen
        while i < pindex and pindex < j :
            while arr[i] < pivot :
                i+=1

            while arr[j] > pivot :
                j-=1
            
            if i < pindex and pindex < j :
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1

        return pindex

    def quicksort(self, arr, l, r):
        if l >= r:
            return
            # make paritions
        p = self.partition(arr, l, r)
        # left sort
        self.quicksort(arr, l, p-1)
        # right sort
        self.quicksort(arr, p+1, r)


arr=[12,5,2,7,15,1]
QS().quicksort(arr, 0, len(arr)-1)
print(arr)