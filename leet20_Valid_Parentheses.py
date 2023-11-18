def isValid(s):
    # User solution, same logic but think in reverse
    charList = []
    for char in s:
        if char == "(":
            charList.append(")")
        elif char == "{":
            charList.append("}")
        elif char == "[":
            charList.append("]")
        elif not charList or charList.pop() != char:
            return False
    
    if charList:
        return False
    else:
        return True
    # My Solution below
    # charList = []
    # for char in s:
    #     if char == ")" and (not charList or (charList and charList.pop() != "(")):
    #         return False
    #     elif char == "}" and (not charList or (charList and charList.pop() != "{")):
    #         return False
    #     elif char == "]" and (not charList or (charList and charList.pop() != "[")):
    #         return False
    #     elif char in ["(","{","["]:
    #         charList.append(char)
    
    # if charList:
    #     return False
    # else:
    #     return True

if __name__ == "__main__":
    s = "{[]}"
    print(isValid(s))