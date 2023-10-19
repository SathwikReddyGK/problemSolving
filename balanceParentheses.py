def balanceParenthesis(s):
    sList = []
    for c in s:
        if bool(sList) and sList[-1] == c:
            sList.pop()
        else:
            sList.append(c)
    
    for val in sList:

if __name__ == "__main__":
    s = ")()(())("
    balanceParenthesis(s)
    
