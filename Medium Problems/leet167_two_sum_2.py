import math
def twoSum(numbers,target):
    # Binary Search solution from a user
    for indx,num in enumerate(numbers):
        difference = target - num

        i,j = 0,len(numbers)-1

        while i<j:
            mid = (1 + i + j)//2

            if numbers[mid] == difference:
                return([indx+1,mid+1])
            elif numbers[mid]<difference:
                i = mid+1
            elif numbers[mid]>difference:
                j = mid-1

        


    # Dictionary Solution from a user
    # indexDict = {}

    # for i,num in enumerate(numbers):
    #     difference = target - num

    #     if difference in indexDict:
    #         return(indexDict[difference]+1,i+1)
    #     else:
    #         indexDict[num] = i

    # Two Pointer Solution from a user
    # i,j = 0,len(numbers)-1
    # while i<j:
    #     sum = numbers[i] + numbers[j]

    #     if sum == target:
    #         return ([i+1,j+1])
    #     elif sum < target:
    #         i += 1
    #     elif sum > target:
    #         j -= 1
    # Two Pointer Solution from my side
    # i = 0
    # j = len(numbers) - 1
    # while j>i:
    #     searchVal = target - numbers[i]

    #     while numbers[j] >= searchVal:
    #         if numbers[j] == searchVal:
    #             return([i+1,j+1])
    #         else:
    #             j -= 1
        
    #     i += 1
                
        
    # Below solution is not good, causes time limit exceeded
    # for i in range(0,len(numbers)):
    #     findVal = target - numbers[i]

    #     for j in range(len(numbers)-1,-1,-1):
    #         if numbers[j] == findVal:
    #             return([i+1,j+1])
    #         elif numbers[j] < findVal or numbers[j] <= numbers[i]:
    #             break

if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    print(twoSum(numbers,target))