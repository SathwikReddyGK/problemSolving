def wordBreak(s, wordDict):
    if "cat" in s:
        return True
    else:
        return False

if __name__ == "__main__":
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print(wordBreak(s,wordDict))