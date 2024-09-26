# Problem
# 763. Partition Labels
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.

# Solution

# // Time Complexity :  O(N)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Greedy Solution - Find the last index of all characters so that when we run on the string again we will know the end index
# once, before going to end if we find any other character whose end index is greater then that becomes end index
# https://www.youtube.com/watch?v=7ly2mpKEVmo

def partitionLabels(s):
    minMaxDict = {}
    result = []

    for i in range(len(s)):
        if s[i] in minMaxDict:
            minMaxDict[s[i]][1] = i
        else:
            minMaxDict[s[i]] = [i,i]
    
    start = 0
    end = None
    for i in range(len(s)):
        if i == end:
            result.append(end - start + 1)
            end = None
            start = i+1
            continue

        if end == None:
            end = minMaxDict[s[i]][1]
            if start == end:
                result.append(1)
                end = None
                start = i+1
                continue
        elif end < minMaxDict[s[i]][1]:
            end = minMaxDict[s[i]][1]
    
    return result

if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    print(partitionLabels(s))