# Description
# You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

# Train tickets are sold in three different ways:

# a 1-day pass is sold for costs[0] dollars,
# a 7-day pass is sold for costs[1] dollars, and
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.

# For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
# Return the minimum number of dollars you need to travel every day in the given list of days.

 

# Example 1:

# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total, you spent $11 and covered all the days of your travel.
# Example 2:

# Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# Output: 17
# Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
# On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
# In total, you spent $17 and covered all the days of your travel.
 

# Constraints:

# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days is in strictly increasing order.
# costs.length == 3
# 1 <= costs[i] <= 1000

# Solution

# // Time Complexity : Iterative approach(just other version of DP): O(n)
#                      DP with recursion approach: O(n)
#                      Exhaustive approach: O(3^n)
# // Space Complexity : Iterative approach(just other version of DP): O(n) for array
#                       DP with recursion approach: O(n) for both array and implicit stack
#                       Exhaustive approach: O(n)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Iterative approach and Recursion with DP. Each number will have three options. Think of solving this from the end

import math

def mincostTickets(days,costs):
    n = len(days)
    maxDay = days[n-1]

    dp = [math.inf for _ in range(maxDay+1)]

    daysSet = set()
    for day in days:
        daysSet.add(day)
    
    for i in range(maxDay,0,-1):
        if i in daysSet:
            if i == maxDay:
                dp[i] = min(costs[0],costs[1],costs[2])
            
            if i+1 > maxDay:
                oneDayPass = costs[0]
            else:
                oneDayPass = costs[0]+dp[i+1]
            
            if i+7 > maxDay:
                sevenDayPass = costs[1]
            else:
                sevenDayPass = costs[1]+dp[i+7]

            if i+30 > maxDay:
                thirtyDayPass = costs[2]
            else:
                thirtyDayPass = costs[2]+dp[i+30]
            
            dp[i] = min(oneDayPass,sevenDayPass,thirtyDayPass)
        else:
            dp[i] = dp[i+1]
    
    return dp[1]

# def helper(self,newDate,n,days,costs,dp):
#     passDays = [1,7,30]
#     for i in range(n):
#         if days[i] <= newDate:
#             continue

#         if dp[i] == math.inf:
#             cost0 = self.helper(days[i],n,days,costs,dp)
#             cost1 = self.helper(days[i]+7-1,n,days,costs,dp)
#             cost2 = self.helper(days[i]+30-1,n,days,costs,dp)
#             dp[i] = min(min(costs[0]+cost0,costs[1]+cost1),costs[2]+cost2)
#             return dp[i]
#         else:
#             return dp[i]     

#         break 

#     return 0         

# def mincostTickets(self, days: List[int], costs: List[int]) -> int:
#     n = len(days)
#     dp = [math.inf for _ in range(n)]
#     self.helper(-math.inf,n,days,costs,dp)
#     return dp[0]

if __name__ == "__main__":
    days = [1,2,3,4,5,6,7,8,9,10,30,31]
    costs = [2,7,15]
    print(mincostTickets(days,costs))