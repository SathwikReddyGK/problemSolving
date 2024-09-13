# Problem
# 20. Valid Parentheses
# Solved
# Easy
# Topics
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# Solution

# // Time Complexity :  O(N)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Use stack and keep track of open bracket, pop when respective close bracket comes up
# https://www.youtube.com/watch?v=e9tAbhSJIuQ

def isValid(s):
    charList = []
    for char in s:
        if char == "(":
            charList.append(")")
        elif char == "{":
            charList.append("}")
        elif char == "[":
            charList.append("]")
        elif not charList or charList.pop() != char:
            return False
    
    if charList:
        return False
    else:
        return True

if __name__ == "__main__":
    s = "([])"
    print(isValid(s))