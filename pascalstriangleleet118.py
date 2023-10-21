def generate(numRows):
    # Solution from a user
    result = [[1]]
    for i in range(1,numRows):
        result.append(list(map(lambda x,y: x+y, result[i-1]+[0],[0]+result[i-1])))
    
    return result
    # Below is my solution
    # result = []

    # for i in range(0,numRows):
    #     iterationres = []
    #     if i == 0:
    #         iterationres.append(1)
    #         result.append(iterationres)
    #     else:
    #         for j in range(0,i+1):
    #             if j == 0 or j == i:
    #                 iterationres.append(1)
    #             else:
    #                 iterationres.append(result[-1][j-1] + result[-1][j])
            
    #         result.append(iterationres)
    
    # return result

if __name__ == "__main__":
    numRows = 5
    print(generate(numRows))