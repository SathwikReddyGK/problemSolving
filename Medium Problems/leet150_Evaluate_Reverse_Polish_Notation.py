# Problem

# 150. Evaluate Reverse Polish Notation
# Medium
# Topics
# Companies
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
 

# Constraints:

# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

# Solution

# // Time Complexity :  O(N)
# // Space Complexity : O(ceil(N/2))
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Keep putting digits in stack, when we get an operator pop the last two digits and perform operation on then, and push the
# result back into stack. Keep performing this till we are at the end of the loop, stack should have the result.
# https://www.youtube.com/watch?v=Z4Byye1zKjQ

from collections import deque
from math import floor
from math import ceil

def evalRPN(tokens):
    numStack = deque()

    for token in tokens:
        if token == "+":
            right = numStack.pop()
            left = numStack.pop()
            numStack.append(left + right)
        elif token == "-":
            right = numStack.pop()
            left = numStack.pop()
            numStack.append(left - right)
        elif token == "*":
            right = numStack.pop()
            left = numStack.pop()
            numStack.append(left * right)
        elif token == "/":
            right = numStack.pop()
            left = numStack.pop()
            result = left / right
            if result >= 0:
                result = floor(result)
            else:
                result = ceil(result)
            numStack.append(result)
        else:
            numStack.append(int(token))
                
    return numStack.pop()

if __name__ == "__main__":
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens))