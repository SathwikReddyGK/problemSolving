# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

# Example 1:

# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
 

# Constraints:

# 0 <= key <= 106
# At most 104 calls will be made to add, remove, and contains.

# // Time Complexity : O(1) for all operations
# // Space Complexity : O(n) since in worst case all the keys are saved in hashset
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : Squareroot, Floor and Ceil was not used at right spot

# // Your code here along with comments explaining your approach
# Approach is to used double hashing technique so that we can split the total entries into buckets
# Using key modulus with sqrt(n) to get the position in main array, then use key/sqrt(n) to find position in bucket array
# This helps avoiding collision while we are still able to access values in O(1) time complexity

# Solution
from math import sqrt
from math import ceil
from math import floor
class MyHashSet:

    def __init__(self):
        self.offset = ceil(sqrt(1000000))
        self.binArray = [None for _ in range(0,self.offset)]
        

    def add(self, key: int) -> None:
        arr1Offset = key%self.offset
        arr2Offset = floor(key/self.offset)
        if self.binArray[arr1Offset] == None:
            if arr1Offset == 0:
                self.binArray[arr1Offset] = [False for _ in range(0,self.offset+1)]
            else:
                self.binArray[arr1Offset] = [False for _ in range(0,self.offset)]
            self.binArray[arr1Offset][arr2Offset] = True
        else:
            self.binArray[arr1Offset][arr2Offset] = True
        

    def remove(self, key: int) -> None:
        arr1Offset = key%self.offset
        arr2Offset = floor(key/self.offset)
        if self.binArray[arr1Offset] != None:
            self.binArray[arr1Offset][arr2Offset] = False
        

    def contains(self, key: int) -> bool:
        arr1Offset = key%self.offset
        arr2Offset = floor(key/self.offset)
        if self.binArray[arr1Offset] == None:
            return False
        elif self.binArray[arr1Offset][arr2Offset] == True:
            return True
        
        return False

if __name__ == "__main__":
    obj = MyHashSet()   
    obj.add(1)
    obj.add(2)
    print(obj.contains(1))
    print(obj.contains(3))
    obj.add(2)
    print(obj.contains(2))
    obj.remove(2)
    print(obj.contains(2))
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)