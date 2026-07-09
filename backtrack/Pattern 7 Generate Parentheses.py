"""
Backtracking pattern: Generate Parentheses

Idea:
- Build a valid parentheses string by choosing to add an opening bracket or a closing bracket at each step.
- The recursion only allows valid states, so invalid strings are pruned early.

Why it works:
- Every path that ends with balanced parentheses is a valid answer.
- The constraints on open and close counts preserve correctness while exploring the search tree.

Time Complexity:
- The number of valid outputs is the Catalan number, approximately 4^n / sqrt(n).
- Each output string has length O(n), so the total work is about O(4^n / sqrt(n)).

Space Complexity:
- The recursion depth is O(n), and the current string also uses O(n).
- Extra space excluding output: O(n)
"""

def backtrack(open_count, close_count, path):

    if open_count==3 and close_count==3:
        print(path)
        return

    if open_count<3:
        backtrack(open_count+1, close_count, path+"(")

    if close_count<open_count:
        backtrack(open_count, close_count+1, path+")")

backtrack(0,0,"")