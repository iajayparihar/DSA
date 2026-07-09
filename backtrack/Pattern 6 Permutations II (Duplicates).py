"""
Backtracking pattern: Permutations II (Duplicates)

Idea:
- This is the same as permutations, but duplicates are handled by skipping equal numbers when they would create the same arrangement.
- Sorting makes duplicate handling easier and more systematic.

Why it works:
- Every unique permutation is generated once because the duplicate-skip rule prevents repeated branches.
- The visited array still ensures each element position is used once.

Time Complexity:
- In the worst case, the number of distinct permutations can still be n!.
- Copying one permutation takes O(n), so the total is O(n * n!).

Space Complexity:
- The recursion depth and current path use O(n) space.
- Extra space excluding output: O(n)
"""

nums=[1,1,2]
nums.sort()

visited=[False]*len(nums)

def backtrack(path):

    if len(path)==len(nums):
        print(path)
        return

    for i in range(len(nums)):

        if visited[i]:
            continue

        if i>0 and nums[i]==nums[i-1] and not visited[i-1]:
            continue

        visited[i]=True
        path.append(nums[i])

        backtrack(path)

        path.pop()
        visited[i]=False

backtrack([])