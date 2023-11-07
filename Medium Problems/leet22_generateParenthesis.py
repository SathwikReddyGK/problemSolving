def generateParenthesis(n):
    res = []

    def dfs(res,temp,open,close,n):
        if len(temp) >= 2*n:
            res.append(temp)
            return

    # My Solution, took 72ms beats just 5.14% of users with python
    # lost my way in between and worked for all entries from 1 pairs of
    # parenthesis to n paris of parenthesis
    # def bfs(begin):
    #     curLen = len(res)
    #     for i in range(begin,len(res)):
    #         for c in range(0,len(res[i])):
    #             if res[i][c] == "(":
    #                 temp = res[i][:c+1] + "()" + res[i][c+1:]
    #                 if temp not in res:
    #                     res.append(temp)
    #         temp = res[i]+"()"
    #         if temp not in res:
    #             res.append(temp)        
    #     return curLen

    # res = []
    # if n<= 0:
    #     return
    
    # temp = "()"
    # res.append(temp)
    # curLen = 0
    # for i in range(1,n):
    #     curLen = bfs(curLen)
    
    # out = res[curLen:].copy()
    # return out


if __name__ == "__main__":
    n = 3
    print(generateParenthesis(n))