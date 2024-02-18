# Description
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

# Constraints:

# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.

# Solution

# // Time Complexity : O(N*K) where K is length of each word
# // Space Complexity : O(N) if we add all elements into queue
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Approach is to use queue to do level order of traversal of the imaginary tree. Use a set to keep track of word list.
# So that search is O(1). For each word, we need to create 26*k where k is word length combinations and then check if each word
# if it is there in set. Word not in set should be ignored. Word in set should be added to queue. Do this 26 letter combination
# for each letter of each word to save time complexity compared to check a word with all the words from worddict which will go to
# O(n^2) solution

from collections import deque
import string

def ladderLength(beginWord, endWord, wordList):

    wordSet = set(wordList)
    wordCheck = deque()

    if endWord not in wordSet:
        return 0
    
    wordCheck.append(beginWord)

    level = 1
    if beginWord in wordSet:
        wordSet.remove(beginWord)
    while wordCheck:
        qsize = len(wordCheck)
        while qsize > 0:
            qsize -= 1
            tempWord = wordCheck.popleft()
            wordLen = len(tempWord)
            for i in range(wordLen):
                wordList = list(tempWord)
                for c in string.ascii_lowercase:
                    if c != tempWord[i]:
                        wordList[i] = c
                        newWord = "".join(wordList)
                        if newWord == endWord:
                            return level+1
                        elif newWord in wordSet:
                            wordCheck.append(newWord)
                            wordSet.remove(newWord)
        
        level += 1
    
    return 0

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(ladderLength(beginWord, endWord, wordList))