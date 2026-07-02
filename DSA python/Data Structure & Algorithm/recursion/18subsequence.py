class SS:
    def subsequence(self,arr,output,index,ans):
        if index >= len(arr):
            if len(output) > 0 :
                ans.append(output)
            return 
        #exclude 
        self.subsequence(arr, output.copy(), index+1, ans)

        element=arr[index]
        output.append(element)
        self.subsequence(arr, output.copy(), index+1, ans)

str1='a'
ans=[]
SS().subsequence(str1, [], 0, ans)
print(ans)
# [['a']] # empty array is not included