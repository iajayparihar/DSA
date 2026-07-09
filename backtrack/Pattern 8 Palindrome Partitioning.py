"""
Backtracking pattern: Palindrome Partitioning

Idea:
- Try every possible substring starting from a position and split it only if it is a palindrome.
- Each valid split leads to a recursive search for the remaining suffix.

Why it works:
- Every complete path corresponds to one partition of the string into palindromic pieces.
- The recursion checks each possible boundary, ensuring all partitions are explored.

Time Complexity:
- The number of partition choices grows exponentially, and each partition can take O(n) to construct.
- Worst-case time: O(n * 2^n)

Space Complexity:
- The current partition path and recursion stack each use O(n) space.
- Extra space excluding output: O(n)
"""

s="aab"

def isPalindrome(x):
    return x==x[::-1]

def backtrack(start,path):

    if start==len(s):
        print(path)
        return

    for end in range(start,len(s)):

        piece=s[start:end+1]

        if isPalindrome(piece):

            path.append(piece)

            backtrack(end+1,path)

            path.pop()

backtrack(0,[])