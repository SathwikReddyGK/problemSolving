def findAllAnagrams(s,p)->[]:

    if len(s) < len(p):
        return []

    pCount = {}
    sCount = {}

    for i in range(0,len(p)):
        pCount[p[i]] = 1 + pCount.get(p[i],0)
        sCount[s[i]] = 1 + sCount.get(s[i],0)
    
    res = [0] if pCount == sCount else []

    for i in range(len(p),len(s)):
        sCount[s[i-len(p)]] -= 1
        if sCount[s[i-len(p)]] == 0:
            sCount.pop(s[i-len(p)])
        sCount[s[i]] = 1 + sCount.get(s[i],0)
        if sCount == pCount:
            res.append(i-len(p)+1)
    
    return res


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(findAllAnagrams(s,p))