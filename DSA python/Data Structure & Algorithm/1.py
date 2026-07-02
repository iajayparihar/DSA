def matchingStrings(stringList, queries):
    # Write your code here
    count=0
    result=[0]*len(queries)
    for i in range(len(queries)):
        for j in range(len(stringList)):
            if queries[i]==stringList[j]:
                count+=1
                result[i]=count
            
    return result

# stringList=["ab","ab","xyz","ab"]
# queries=["ab","xyz","bc"]
# a=matchingStrings(stringList, queries)
# print(a)
var1 = 1
var2 = 2
var3 = "3"
b=var1+var3
print(b)
a=list(var1,var2,var3)
print(a)
print(var1 + var2 + var3)