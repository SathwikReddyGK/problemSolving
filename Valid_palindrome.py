def isPalindrome(s: str) -> bool:
    iter = len(s)-1
    for start in range(0,len(s)-1):
        charS = s[start]
        if(charS.isalnum()):
            if(charS.isupper()):
                charS = charS.lower()
            for end in range(iter,start,-1):
                charE = s[end]
                if(charE.isalnum()):
                    if(charE.isupper()):
                        charE = charE.lower()
                    if(charS != charE):
                        print("start:",charS,", end:",charE)
                        return False
                    else:
                        iter = end-1
                        if(iter == start):
                            return True
                        break
                    
    
    return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))