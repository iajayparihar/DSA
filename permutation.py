from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path):
            
            if len(path[:]) == len(nums):
                res.append(path[:])
                return
            
            for _ , num in enumerate(nums):
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()

        backtrack([])
        return res
    
a  = Solution()
print(a.permute([1,2,3]))