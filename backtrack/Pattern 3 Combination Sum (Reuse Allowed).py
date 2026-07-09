"""
Backtracking pattern: Combination Sum (Reuse Allowed)

Idea:
- At each step, try every candidate from the current index onward and reduce the remaining target.
- Since reuse is allowed, the same index can be chosen again in the next recursive call.

Why it works:
- Every valid branch reaches target 0 with a combination that meets the sum requirement.
- Reusing the same candidate is allowed, so the search explores different ways to build the target.

Time Complexity:
- The search tree grows exponentially with the target value, so the runtime is exponential in the target size.
- In common interview notation this is written as O(2^t) or more generally exponential in the target.

Space Complexity:
- The recursion depth is at most the number of chosen elements, which is O(t) in the worst case.
- Extra space excluding output: O(t)
"""

nums = [2,3,6,7]

def backtrack(start, target, path):
    if target == 0:
        print(path)
        return

    if target < 0:
        return

    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i, target - nums[i], path)
        path.pop()

backtrack(0, 7, [])