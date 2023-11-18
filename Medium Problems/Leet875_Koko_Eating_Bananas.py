import math
def minEatingSpeed(piles,h):
        # User solution, same as Neetcode but instead of sort, just use
        # max function so that complexity will be from nlogn to n to find
        # rangeEnd. But overall complexity remains same since below loop complexity will be greater               
        rangeStart = 1
        rangeEnd = max(piles)
        
        current = 0
        while rangeStart <= rangeEnd:
            mid = (rangeStart + rangeEnd)//2
            sum = 0
            for num in piles:
                sum += math.ceil(num/mid)

            if sum<=h:
                current = mid
                rangeEnd = mid-1
            else:
                rangeStart = mid+1
        
        return current
        # Neetcode solution
        # piles.sort()
                
        # rangeStart = 1
        # rangeEnd = piles[-1]
        
        # current = 0
        # while rangeStart <= rangeEnd:
        #     mid = (rangeStart + rangeEnd)//2
        #     sum = 0
        #     for num in piles:
        #         sum += math.ceil(num/mid)

        #     if sum<=h:
        #         current = mid
        #         rangeEnd = mid-1
        #     else:
        #         rangeStart = mid+1
        
        # return current
        # Below solution does not work because when selecting range
        # I forgot that koko can eat a pile in an hour and nothing more
        # so cant really split values between piles
        # piles.sort()
        # sum = 0
        # for num in piles:
        #     sum += num
        
        # rangeStart = 0
        # rangeEnd = 0
        # for i in range(len(piles)):
        #     if (sum/piles[i]) < float(h):
        #         rangeStart = piles[i-1]
        #         rangeEnd = piles[i]
        #         break

        # current = 0
        # print(rangeStart,rangeEnd)
        # while rangeStart <= rangeEnd:
        #     mid = (rangeStart + rangeEnd)//2
        #     days = math.ceil(sum/mid)
        #     if days == h:
        #         return mid
        #     elif days<h:
        #         current = mid
        #         rangeEnd = mid-1
        #     else:
        #         rangeStart = mid+1
        
        # return current

if __name__ == "__main__":
     piles = [3,6,7,11]
     h = 8
     print(minEatingSpeed(piles,h))