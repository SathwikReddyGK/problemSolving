def superReducedString(s):
    # Write your code here
    charStack = []
    
    for c in s:
        if charStack and charStack[-1][0] == c:
            charStack[-1][1] += 1
            if charStack[-1][1] == 2:
                charStack.pop()
        else:
            charStack.append([c,1])
    
    print(charStack)
    # if charStack:
    # return "".join(c charStack[][0])
    # else:
    #     return str()

if __name__ == '__main__':
    s = "aa"
    print(superReducedString(s))