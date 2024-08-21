def findJudge(n,trust):
    auxArray = [0]*(n+1)

    for edge in trust:
        auxArray[edge[0]] -= 1
        auxArray[edge[1]] += 1
    
    for i in range(1,n+1):
        if auxArray[i] == n-1:
            return i
    
    return -1

if __name__ == "__main__":
    # n = 2
    # trust = [[1,2]]
    n = 3
    # trust = [[1,3],[2,3]]
    trust = [[1,3],[2,3],[3,1]]
    print(findJudge(n,trust))