def isAnagram(s: str, t: str) -> bool:
    # One more solution by a user
    if len(s) != len(t):
         return False
    
    for c in set(s):
        if s.count(c) != t.count(c):
            return False
    
    return True
    # Other solution by a user
    # temp1 = list(s)
    # temp2 = list(t)
    # temp1.sort()
    # temp2.sort()

    # if temp1 != temp2:
    #      return False
    # return True

    # Solution by a user
    # if len(s) != len(t):
    #     return False
    # chardict = {}

    # for c in s:
    #     item = chr(ord(c) - ord('a'))
    #     if item in chardict:
    #         chardict[item] += 1
    #     else:
    #         chardict[item] = 1
    
    # for c2 in t:
    #     item = chr(ord(c2) - ord('a'))
    #     if item in chardict:
    #         chardict[item] -= 1
    #     else:
    #         return False

    # for check in chardict:
    #     if chardict[check] != 0:
    #         return False
    
    # return True
    

    # Solution below is Mine
    # temp = t
    # if len(s) != len(t):
    #     return False
    # else:
    #     for c in s:
    #         if c not in temp:
    #             return False
    #         index = temp.index(c)
    #         temp = temp[:index]+temp[index+1:len(temp)]
    #     return True

if __name__ == "__main__":
     s = "anagram"
     t = "nagaram"
     print(isAnagram(s,t))