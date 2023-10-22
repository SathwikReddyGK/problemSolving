def hammingweight(n):
    # User solution 2
    count = 0
    while n:
        # below line removes the right most 1 from n
        n &= n-1
        count += 1
    
    return count
    # User solution
    # ans = 0
    # while n:
    #     n &= (n-1)
    #     ans += 1
    # return ans
    # My solution but bitwise operation(doesnt work in local system, only in leetcode)
    count = 0
    while n>0:
        print(n)
        
        if n & 1 == 1:
            count += 1
        n >>= 1
    
    # return count
    # My solution
    # count = 0
    # while True:
    #     val = n%10
    #     n = n//10
    #     if val == 1:
    #         count+=1
    #     if n == 0:
    #         break

    # return count

if __name__ == "__main__":
    n = 11111111111111111111111111111101
    print(hammingweight(n))