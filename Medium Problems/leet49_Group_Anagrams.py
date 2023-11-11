from collections import defaultdict
def groupAnagrams(strs):
    # Solution suggested by Sudharshan and Suhas
    sortedDict = defaultdict(list)

    for str in strs:
        sortedStr = ''.join(sorted(str))
        sortedDict[sortedStr].append(str)
    
    return sortedDict.values()

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))