class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        for j in nums:
            if j not in nums[:i]:
                nums[i]=j
                i+=1
            print(nums[:i])

        mylist=list(set(nums))    
        print(mylist)
        
        return i
k=Solution()
nums = [2,2,3,3,3,3,4,5,5,5,5,6]
# x=nums[:0]
# print(x)
a=k.removeDuplicates(nums)
print(a)