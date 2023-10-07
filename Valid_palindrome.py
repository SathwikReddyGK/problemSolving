def isPalindrome(s: str) -> bool:
    
    #Solution 3 from same user
    i,j = 0,len(s)-1
    while j>i:
        if(s[i].isalnum() and s[j].isalnum()):
            if(s[i].lower() != s[j].lower()):
                return False
            else:
                i,j = i+1,j-1
        i,j = i + (not s[i].isalnum()), j-(not s[j].isalnum())
    return True

    #Below is solution 2 from a user
    # s = [i for i in s.lower() if i.isalnum()]
    # return s == s[::-1]

    # OLD Solution is below, I kind of know Git saves the version, just testing how it works first before effectively using the version control with no fear of loosing old code
    # iter = len(s)-1
    # for start in range(0,len(s)-1):
    #     charS = s[start]
    #     if(charS.isalnum()):
    #         if(charS.isupper()):
    #             charS = charS.lower()
    #         for end in range(iter,start,-1):
    #             charE = s[end]
    #             if(charE.isalnum()):
    #                 if(charE.isupper()):
    #                     charE = charE.lower()
    #                 if(charS != charE):
    #                     print("start:",charS,", end:",charE)
    #                     return False
    #                 else:
    #                     iter = end-1
    #                     if(iter == start):
    #                         return True
    #                     break
                    
    
    # return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))