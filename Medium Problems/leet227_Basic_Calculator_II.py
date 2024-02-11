# Description
# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "3+2*2"
# Output: 7
# Example 2:

# Input: s = " 3/2 "
# Output: 1
# Example 3:

# Input: s = " 3+5 / 2 "
# Output: 5
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# The answer is guaranteed to fit in a 32-bit integer.

# Solution

# // Time Complexity : Stack Approach: O(2N) it is almost like we are going over the string twice, since we are storing everything
#                      in stack and popping it all again in the end to add it
#                      Variable Approach: O(N) we just iterate over the string characters once
# // Space Complexity : Stack Approach: O(N) since we save each number in stack and process the values when we get *
#                       Variable Approach: O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : Floor division, should remember that if numerator is negative, then flooring
# takes value to smaller value leading to taking -2.5 to -3 instead of -2. Remember to skip spaces. Remember that we might
# get double/tirple/more digits so use lv_curr*10 + string[i] to form multiple digits.


# // Your code here along with comments explaining your approach
# Stack Approach
# We can keep appending the numbers into stack with their sign, the moment we come across "*" or "/" we need to pop the previous
# value, perform the operation and add it back to stack. Once the entire string is processed, we need to just go over the entire
# stack and take a sum to get the result
# Variable Approach
# We should use four temp variables to hold current value, operation pending to be performed, tail value(needed to remove from
# calculated value, if we come across division or multiplication). As we iterate over array, remember to skip spaces and we might
# get double/tirple/more digits so use lv_curr*10 + string[i] to form multiple digits.
import math
def handleOp(valStack,lv_op,lv_curr):
    if lv_op == "*":
        temp = valStack.pop()
        valStack.append(temp * lv_curr)
    elif lv_op == "/":
        temp = valStack.pop()
        if (temp<0 or lv_curr<0) and (temp>0 or lv_curr>0):
            # temp *= -1
            valStack.append(math.ceil(temp/lv_curr))
        else:
            valStack.append(temp//lv_curr)
    elif lv_op == "-":
        valStack.append(-lv_curr)
    elif lv_op == "+":
        valStack.append(lv_curr)

def calculate(s):
    # S30 using stack
    valStack = []
    lv_op = "+"
    lv_curr = 0
    n = len(s)
    result = 0
    for i in range(n):
        if s[i] == " ":
            continue
        if i == n-1:
            lv_curr = lv_curr*10 + int(s[i])
            handleOp(valStack,lv_op,lv_curr)
            lv_op = ""
            lv_curr = 0
            continue
        
        if s[i].isdigit():
            lv_curr = lv_curr*10 + int(s[i])
        else:
            lv_tempOp = lv_op
            lv_op = s[i]
            # valStack.append(lv_curr)
            handleOp(valStack,lv_tempOp,lv_curr)
            lv_curr = 0
    
    if lv_op == "*" or lv_op == "/" or lv_curr != None:
        handleOp(valStack,lv_op,lv_curr)
    
    while valStack:
        result += valStack.pop()
    
    return result

    # S30 Using Variables
    # lv_opp = "+"
    # lv_calc = 0
    # lv_curr = 0
    # lv_tail = 0
    # n = len(s)
    # lv_tempOpp = None
    # for i in range(0,n+1):
    #     if i == n:
    #         lv_tempOpp = lv_opp
    #     elif s[i] == " ":
    #         continue
    #     elif not s[i].isdigit():
    #         lv_tempOpp = lv_opp
    #         lv_opp = s[i]
    #     else:
    #         lv_tempOpp = None
        
    #     if lv_tempOpp == "+":
    #         lv_calc = lv_calc + lv_curr
    #         lv_tail = lv_curr
    #         lv_curr = 0
    #     elif lv_tempOpp == "-":
    #         lv_calc = lv_calc - lv_curr
    #         lv_tail = -lv_curr
    #         lv_curr = 0
    #     elif lv_tempOpp == "*":
    #         lv_calc = lv_calc - lv_tail + (lv_tail * lv_curr)
    #         lv_tail = lv_tail * lv_curr
    #         lv_curr = 0
    #     elif lv_tempOpp == "/":
    #         if lv_tail < 0:
    #             lv_tail *= -1
    #             lv_bodmas = (lv_tail//lv_curr)
    #             lv_tail *= -1
    #             lv_bodmas *= -1
    #         else:
    #             lv_bodmas = (lv_tail//lv_curr)
    #         lv_calc = lv_calc - lv_tail + lv_bodmas
    #         if lv_tail < 0:
    #             lv_tail *= -1
    #             lv_tail = (lv_tail//lv_curr)
    #             lv_tail *= -1
    #         else:
    #             lv_tail = (lv_tail//lv_curr)
    #         lv_curr = 0
    #     else:
    #         lv_curr = lv_curr*10 + int(s[i])
    
    # return lv_calc

if __name__ == "__main__":
    s = "415+21*3*3*2+7551/3-4*39*15/2/3-37705*2/3/2*4/24/2-204+4140"
    print(calculate(s))