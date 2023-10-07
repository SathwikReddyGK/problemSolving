def reverseString(s:list[str]) -> None:
    
    # Solution from a user
    s[:] = s[::-1]
    print(s)
    # Solution one(Mine)
    # i,j = 0,len(s)-1
    # while j>i:
    #     extraMem = s[i]
    #     s[i] = s[j]
    #     s[j] = extraMem
    #     i,j = i+1,j-1
    # print(s)

if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    reverseString(s)

