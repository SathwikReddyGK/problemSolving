# Description
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
 

# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.

# Solution

# // Time Complexity : O(n) where n is length of string not pattern, since pattern is generally smaller than string
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Approach is to save each character of pattern with it's respective word coming from the string. Saving that in dictionary,
# this helps us to check if the same word is used in string if the same key from pattern is coming up

def wordPattern(pattern, s):
    lenS = len(s)
    patternDict = {}
    tempIndex = 0
    spaceCount = 0

    for pStr in pattern:
        word = ""
        for i in range(tempIndex,lenS):
            if s[i] == " ":
                spaceCount += 1
                tempIndex = i+1
                break
            word += s[i]

        if pStr in patternDict:
            if patternDict[pStr] != word:
                return False
        else:
            if word in patternDict.values():
                return False
            patternDict[pStr] = word  

    if spaceCount != len(pattern) - 1:
            return False

    return True


if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    print(wordPattern(pattern,s))