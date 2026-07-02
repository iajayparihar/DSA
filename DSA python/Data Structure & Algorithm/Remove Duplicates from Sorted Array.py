class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # len_numb=len(nums)
        # mylist=list(set(nums))
        # len_new_list=len(mylist)
        # l=[0]*len_new_list
        i=0
        for j in nums:
            if j not in nums[:i]:
                nums[i]=j
                i+=1
        print(nums)
        # l[i]=mylist[i]
        # print(len_new_list,l)
        # return len_new_list
k=Solution()
nums = [2,2,3,3,3,3,4,5,5,5,5,6]
a=k.removeDuplicates(nums)
print(a)