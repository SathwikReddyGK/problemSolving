# Description
# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

 

# Example 1:

# Input: order = "cba", s = "abcd"
# Output: "cbad"
# Explanation: 
# "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
# Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
# Example 2:

# Input: order = "cbafg", s = "abcd"
# Output: "cbad"
 

# Constraints:

# 1 <= order.length <= 26
# 1 <= s.length <= 200
# order and s consist of lowercase English letters.
# All the characters of order are unique.

# Solution

# // Time Complexity : Optimized: O(m) m is the length of string, the order array can be max of 26 so it will be constant
# // Space Complexity : O(1) since at max there can be just 26 characters
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Optimized Solution: Iterate over string once by saving frequency of each characters in dictionary. Once done, iterate over the 
# order array and print the each character of order by taking the frequency from dictionary. Rest of the characters which are
# not in the order array can be printed in any order
# Bruteforce Approach: Is checking all possibilites to see if the pattern matches

def customSortString(order,s):
    charDict = {}
    result = ""

    for c in s:
        if c in charDict:
            charDict[c] += 1
        else:
            charDict[c] = 1
    
    for c in order:

        if c in charDict:
            count = charDict[c]

            while count>0:
                result += c
                count -= 1
            del charDict[c]
    
    for charDictitem in charDict.items():
        c = charDictitem[0]
        count = charDictitem[1]
        while count>0:
            result += c
            count -= 1
    
    return result

if __name__ == "__main__":
    order = "cbafg"
    s = "abcd"
    print(customSortString(order,s))        