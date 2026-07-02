class phone:
    def key(self,arr,output,index,ans,mapping):
        if index >=len(arr):
            ans.append(output)
            return
        number=int(arr[index])
        value=mapping[number]
        for i in range(len(value)):
            output.append(value[i])
            self.key(arr, output.copy(), index+1, ans, mapping)
            output.pop()


def fun(arr,output,index,ans,mapping):
    if index >= len(arr):
        ans.append(output)
        return 

    ele = int(arr[index])
    letters = mapping[ele]

    for i in letters:
        output.append(i)
        fun(arr, output.copy(), index+1, ans, mapping)
        output.pop()

    
mapping=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
digits='23'
index=0
ans1=[]
output=[]
# class base fun call
phone().key(digits, output, index, ans1, mapping)


# function base
ans2=[]
fun(digits, output, index, ans2, mapping)


if ans1 == ans2:
    print('both functions is doing well')
else:
    print('error')