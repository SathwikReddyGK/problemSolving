# Description
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 

# Constraints:

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

# Solution

# // Time Complexity : Recurson with DP approach O(n^2)
#                      Exhaustive Time Limit Exceeded recursion approach O(n^n), at each level we will have to check all n 
#                      combinations of letters. Similarly at the maximum of n levels if each character is in dictionary.
# // Space Complexity : Exhaustive Time Limit Exceeded approach O(n^2) where n is the max number of levels since each character
#                       can be in the dictionary. And at each level we will be checking if there are n combinations
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Exhaustive approach, from left to right check if a letter exists in the dictionary. If a letter exists
# then from the next letter you repeat the same thing. If a letter does not exist then combintaion of the letter and next letter
# will have to be checked, keep increasing the number of letters till you find a combination available in dictionary. If none of 
# the combinations work then return False, else return True.

def wordBreak(s, wordDict):
    n = len(s)
    dp = [False for _ in range(n+1)]
    wordSet = set(wordDict)

    dp[0] = True
    j = 0

    for i in range(n):
        j = 0
        while j<=i:

            if j == 0 or dp[j] == True:
                tempStr = s[j:i+1]
                if tempStr in wordSet:
                    dp[i+1] = True
                    break

            j += 1
    
    return dp[n]
    # def helper(self,s,pivot,n,wordSet):
    #     if pivot > n-1:
    #         return True
    #     for i in range(pivot,n):
    #         strVar = s[pivot:i+1]
    #         if strVar in wordSet and self.helper(s,i+1,n,wordSet):
    #             return True
        
    #     return False

    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     wordSet = set()
    #     n = len(s)

    #     for string in wordDict:
    #         wordSet.add(string)
        
    #     return self.helper(s,0,n,wordSet)

if __name__ == "__main__":
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print(wordBreak(s,wordDict))