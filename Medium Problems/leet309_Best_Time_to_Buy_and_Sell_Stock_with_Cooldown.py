def maxProfit(prices):
    # neetcode approach, implementing it
    
    # Below is my solution, which is giving time limit exceeded for 207/210 case
    # (prices = [48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94])
    
    # resList = []

    # if len(prices) <= 1:
    #     return 0

    # def dfs(begin,win):
    #     temp = win
    #     if begin >= len(prices)-1:
    #         return win
    #     for i in range(begin,len(prices)-1):
    #         for j in range(i+1,len(prices)):
    #             temp += prices[j] - prices[i]
    #             if temp != None and temp > 0:
    #                 resList.append(temp)
    #             app = dfs(j+2,temp)
    #             if app != None:
    #                 resList.append(app)
    #             temp = win
        
    # dfs(0,0)
    # resList.sort()
    # result = resList[-1]
    # if result < 0:
    #      result = 0
    # return result
if __name__ == "__main__":
    # prices = [1,2,3,0,2]
    # prices = [1,11,2,7,4]
    prices = [48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94]
    print(maxProfit(prices))