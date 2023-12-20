# # Description
# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
 

# Constraints:

# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.
 

# Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
# // Time Complexity : O(1) in amortized time for all functions. Peek and Pop might take more time once in a while to copy data from one stack to other
# // Space Complexity : O(n) since we are always saving max of n elements though we are using two stacks. We can consider it as O(2n) if we are using fixed length stack/list
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None

# // Your code here along with comments explaining your approach
# Approach is to create two stacks, one for input and one for output. Pop all the values from input to output when Pop/Peek is called
# This makes sure all the values pushed so far are put in the reverse order to output, this giving us data in FIFO order in output
# Output is not empty, then there are still elements to be poped in order they came, before we have to copy the rest of the items from input,
# That is the reason behind copying from input to output only when output is empty

# Solution
class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
        

    def push(self, x: int) -> None:
        self.input.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.output.pop()
        

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        
        return self.output[-1]
        

    def empty(self) -> bool:
        if not self.input and not self.output:
            return True
