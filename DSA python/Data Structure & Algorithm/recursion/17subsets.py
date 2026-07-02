class ST:
    def subset(self,arr,output,i,ans):
        # base case 
        if i >= len(arr):
            ans.append(output)
            return 
        # exclude
        #   output pass by value
        self.subset(arr, output.copy(), i+1, ans)
        # include
        element=arr[i]
        output.append(element)
        self.subset(arr, output.copy(), i+1, ans)
    
    def sbset(self,arr):
        b=[]
        if not arr:
            b.append(arr)
        else:
            first=arr[0]
            second=arr[1:]
            for x in self.sbset(second):
                b.append(x)
                c=[first]+x
                b.append(c)
        return b 

arr=[4,8,9]
ans=[]
i=0
output=[]
ST().subset(arr, output, i, ans)
print(ans)
print(len(ans))
print()
print()
ans=ST().sbset(arr)
print(ans)
print(len(ans))
