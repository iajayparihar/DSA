class Bubble:
    def sort(self,arr,n):
        #base case

        if n==0 or n==1 :
            return  
        
        # one case solve
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        return self.sort(arr, n-1)

arr=[4,5,3,1,2]
Bubble().sort(arr, 5)
print(arr)

