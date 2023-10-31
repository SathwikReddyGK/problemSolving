def permute(A):
    def backtracking(sol):
        if len(sol) == len(A):
            yield sol.copy()
        for element in A:
            if element not in sol:
                print("before",sol)
                # for i in backtracking(sol+[element]):
                #     print(i)
                yield from backtracking(sol+[element])
                print("after",sol)
    list = []
    # yield from backtracking(list)
    for i in backtracking(list):
        print(i)
    
    # # User solution, recursion with swap, might save memory
    # res = []
    # def dfs(A,begin):
    #     if begin >= len(A):
    #         return res.append(A.copy())
    #     else:
    #         for i in range(begin,len(A)):
    #             A[i],A[begin] = A[begin],A[i]
    #             dfs(A,begin+1)
    #             A[i],A[begin] = A[begin],A[i]
    
    # dfs(A,0)
    # return res
    # Implementing the same solution from my side
    # answer = []
    # stack = []

    # def dfs():
    #     if len(stack) == len(A):
    #         return answer.append(stack.copy())
    #     for i in A:
    #         if i not in stack:
    #             stack.append(i)
    #             dfs()
    #             stack.pop()

    # dfs()
    # return answer

    # Solution by Joey(Zhengyuan Zhu), IDIR
    # ans = []
    # stk = []
    # def dfs(i):
    #     if len(stk)==len(A): 
    #         return ans.append(stk.copy())
    #     for i in range(len(A)):
    #         if A[i] not in stk:
    #             stk.append(A[i])
    #             dfs(i+1)
    #             stk.pop()

    # dfs(0)
    # return ans
    # returnList = []
    # for num in nums:
    #     numList = [num]
    #     for num2 in nums:
    #         if num != num2:
    #             numList.append(num2)
        
    #     returnList.append(numList)
    
    # return returnList


if __name__ == "__main__":
    nums = [1,2,3,4]
    for i in permute(nums):
        pass
        # print(i, end=" ")
    # print(iter(permute(nums)))