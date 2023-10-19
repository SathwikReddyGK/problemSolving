def mostCommonWord(paragraph: str, banned: list[str]) -> str:
        strList = []
        strDict = {}

        temp = ""
        for i in paragraph:
            if ord(i.lower()) in range(ord('a'),ord('z')+1):
                temp += i.lower()
            elif temp != "":
                strList.append(temp)
                temp = ""

        if temp != "":
            strList.append(temp)

        # strList = paragraph.split(" ")
        for i in range(0,len(strList)):
            valCount = banned.count(strList[i].lower())
            if valCount <= 0:
                if strList[i].lower() in strDict:
                    strDict[strList[i].lower()] += 1
                else:
                    strDict[strList[i].lower()] = 1
        
        # return strDict
        strSorted = sorted(strDict.items(), key=lambda item: item[1], reverse=True)
        return strSorted[0][0]

if __name__ == "__main__":
     s = "Bob hit a ball, the hit BALL flew far after it was hit."
     listBan = ["hit"]
     print(mostCommonWord(s,listBan))
