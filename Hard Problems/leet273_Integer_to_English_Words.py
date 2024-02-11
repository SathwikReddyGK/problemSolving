# Description
# Convert a non-negative integer num to its English words representation.

 

# Example 1:

# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:

# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:

# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

# Constraints:

# 0 <= num <= 231 - 1

# Solution

# // Time Complexity : O(1) Since maximum size is 2^31 - 1, maximum depth of division is three 
# // Space Complexity : O(1) Since maximum size is 2^31 - 1, maximum depth of division is three 
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Have three lists, one list for number less than 20, one for all the tens and one for the million, billion and thousand.
# Using modulus and division and recursion we can map the numbers and lists to find the exact number to string conversion

thousand = ["","Thousand","Million","Billion"]
tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
def numberToWords(num):
    result = ""
    i = 0
    if num == 0:
        return "Zero"
    while num>0:
        val = num%1000
        if val>0:
            result = helper(val).strip() + " " + thousand[i] + " " + result
        num = num//1000
        i += 1
    return result.strip()

def helper(val):
    if val<20:
        return lessThan20[val]
    elif val<100:
        return tens[val//10]+ " " + helper(val%10).strip()
    elif val<1000:
        return helper(val//100).strip() + " " + "Hundred" + " " + helper(val%100).strip()

if __name__ == "__main__":
    num = 50868
    print(numberToWords(num))