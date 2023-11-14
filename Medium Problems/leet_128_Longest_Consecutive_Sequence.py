
from collections import defaultdict

def longestConsecutive(nums):
    # User solution, copied to test and see how it works
    mp=defaultdict(list)
    bl=defaultdict(bool)
    mx=0
    for i in nums:
        if bl[i]:
            continue 
        bl[i]=True
        l,r=i,i
        if mp[i+1]:
            r=mp[i+1][0]
        if mp[i-1]:
            l=mp[i-1][1]
        mp[r]=[r,l]
        mp[l]=[r,l]
        mx=max(mx,r-l+1)
        print("i: ",i)
        print("mx: ",mx)
        print("mp: ",mp)
        print("r: ",r)
        print("l: ",l)
    return mx
    # Neetcode logic
    # Put values into set so that we are only running on unique elements of the set
    # Then, since we need to find longest consequitive elements, there must be an element which doesn't
    # have previous element[Eg: if there is [10,100,5,9,8,6,7]], in this sequence is 5,6,7,8,9,10. So
    # we will have 5 as first element. So we find such element whose previous number is not in set. Then
    # increment each time and check if next element exists. If exists then keep incrementing, get the highest lenght
    # then check with next sequence and take the maximum length
    # length = 0
    # maxLength = 0
    # for num in nums:
    #     if num-1 not in nums:
    #         while num+length in nums:
    #             length += 1
    #         maxLength = max(maxLength,length)
    
    # return maxLength


# Below logic is not working, check again
# def longestConsecutive(nums):
#     numDict = {}
#     generatedDicts = []
#     tempDict = {}
#     max_count = 0
#     count = 0

#     def decrement(num):
#         nonlocal count
#         if num not in numDict:
#             return

#         for i in range(0,len(generatedDicts)):
#             if num in generatedDicts[i]:
#                 return
        
#         decrement(num-1)
#         tempDict[num] = 1
#         count += 1

#     def increment(num):
#         nonlocal count
#         if num not in numDict:
#             return

#         for i in range(0,len(generatedDicts)):
#             if num in generatedDicts[i]:
#                 return
        
#         decrement(num+1)
#         tempDict[num] = 1
#         count += 1

#     for num in nums:
#         numDict[num] = 1
    
#     for num in numDict.keys():
#         print(generatedDicts)
#         for i in range(0,len(generatedDicts)):
#             if num in generatedDicts[i]:
#                 return
            
#         decrement(num-1)
#         tempDict[num] = 1
#         count += 1
#         increment(num+1)
#         generatedDicts.append(tempDict)
#         tempDict.clear()
#         max_count = max(max_count,count)
#         count = 0
    
#     return max_count

if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    print(longestConsecutive(nums))