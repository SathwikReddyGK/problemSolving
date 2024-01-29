# Description
# Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

# perm[i] is divisible by i.
# i is divisible by perm[i].
# Given an integer n, return the number of the beautiful arrangements that you can construct.

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: 
# The first beautiful arrangement is [1,2]:
#     - perm[1] = 1 is divisible by i = 1
#     - perm[2] = 2 is divisible by i = 2
# The second beautiful arrangement is [2,1]:
#     - perm[1] = 2 is divisible by i = 1
#     - i = 2 is divisible by perm[2] = 1
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 15

# Solution

# // Time Complexity : O(n!) - Factorial since we need to check almost all permuations to decide if the result is Beautiful
# // Space Complexity : O(n) max size of implicit stack due to recursion
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : Made a mistake on deciding global/local variable. The check on deciding if path is
# complete I had done it before checking the validity of last element added to list, resulting in giving more answers than actual


# // Your code here along with comments explaining your approach
# Approach is to use a backtracking(with for loop based recurison) to come up with all the possible permutations. But for each
# permuation, as we are adding the element we can keep checking if that is satisfying the beautiful conditions, if not then just
# return and ignore that particular permutaion. This helps save some time. If the first element itself is not working then we come
# out

count = 0
def countArrangement(n):
    input = [i+1 for i in range(n)]
    indexDict = {}
    global count
    count = 0    

    def helper(input,indexDict,n,path):
        global count
        
        index = len(path)
        if index>0 and path[index-1]%index != 0 and index%path[index-1] != 0:
            return

        if len(path) == n:
            count += 1
            return

        for i in range(n):
            if i not in indexDict:
                path.append(input[i])
                indexDict[i] = True
                helper(input,indexDict,n,path)
                del indexDict[i]
                path.pop()

    helper(input,indexDict,n,[])
    return count

if __name__ == "__main__":
    n = 4
    print(countArrangement(n))