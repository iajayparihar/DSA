class Strev:
    def rev(self,l,r,arr):
        if l > r :
            return arr 
        arr[l],arr[r]=arr[r],arr[l]
        return self.rev(l+1, r-1, arr)

str='Abhigyan'
arr=list(str)
ans=Strev().rev(0, len(arr)-1 ,arr)
print(''.join(ans))