"""
Backtracking pattern: Permutations

Idea:
- Build a permutation by placing one element at a time and marking used positions.
- Each recursive level chooses one unused number.

Why it works:
- Every complete path from the root to a leaf corresponds to one valid permutation.
- The visited array ensures each element is used exactly once in every permutation.

Time Complexity:
- There are n! permutations of n elements.
- Building one permutation takes O(n), so the total is O(n * n!).

Space Complexity:
- The recursion depth is O(n), and the current path also uses O(n).
- Extra space excluding output: O(n)
"""

nums = [1,2,3]
visited = [False]*len(nums)

def backtrack(path):

    if len(path)==len(nums):
        print(path)
        return

    for i in range(len(nums)):

        if visited[i]:
            continue

        visited[i]=True
        path.append(nums[i])

        backtrack(path)

        path.pop()
        visited[i]=False

backtrack([])