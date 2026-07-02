class LinearSearch:
    def search(self,key,arr,length):
        if length == 0 :
            return False
        
        if key == arr[0] :
            return True
        else:
            arr.pop(0)
            return self.search(key, arr, length-1)

arr=[1,2,3,4,5]
key=1
ans=LinearSearch().search( key , arr , len(arr) )
print(ans)
