class Sorted:
    def isSorted(self,arr,length,n):
        if length == 0 or length == 1 :
            return True
        if arr[n] > arr[n+1]:
            return False
        else:
            return self.isSorted(arr,length-1,n+1)


arr=[1,2,3,4,5,5,5]
if (Sorted().isSorted(arr,len(arr),0)):
    print('Array is Sorted!!')
else:
    print('Array is NOT Sorted!!')
