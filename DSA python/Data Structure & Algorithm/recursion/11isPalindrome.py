class Paindrome:
    def ispalin(self,arr,newPa,l,r):
        if l>r:
            return True

        arr[l],arr[r]=arr[r],arr[l]
        if arr != newPa :
            return False
        else:
            return self.ispalin(arr, newPa, l+1,r-1)

    def isPa(self,arr,l,r):
        if l>r:
            return True

        if arr[l] != arr[len(arr)-l-1] :
            return False
        else:
            return self.isPa(arr,l+1,r-1)

str='12110.'
arr=list(str)

ans=Paindrome().ispalin(arr.copy(), arr.copy(), 0, len(str)-1 )
print(ans)

ans=Paindrome().isPa(arr, 0, len(arr)-1)
print(ans)
