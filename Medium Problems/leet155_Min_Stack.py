# Problem Description
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

# Solution

# // Time Complexity : All operations are O(1)
# // Space Complexity : O(n) since using a stack to save all the elements
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : Had to look at the solution and implement this, did not realise I could have just
# used one more field to maintain minimum. Had missed updating min value when poping(incase poped value is min)


# // Your code here along with comments explaining your approach
# Approach is to use a stack, in class maintain a field called min to have the mininmum value maintained. During push, if the received
# value is mininmum, push the previous minimum first before pushing the new value and update min with new value. This is needed
# to retrieve/pop the previous min if the current value/min is popped out of stack. So handled this in push and pop

from math import inf
class MinStack:
    _min = None
    def __init__(self):
        self.stack = []     
        self.min = float(inf)   

    def push(self, val: int) -> None:
        if self.min >= val:
            self.stack.append(self.min)
            self.stack.append(val)
            self.min = val
        else:
            self.stack.append(val)
        

    def pop(self) -> None:
        popVal = self.stack.pop()
        if popVal == self.min:
            self.min = self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        

if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(2)
    obj.push(-3)
    print(obj.getMin())
    print(obj.pop())
    print(obj.top())
    print(obj.getMin())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()