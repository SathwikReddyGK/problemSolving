# Question
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

# Example 1:

# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
 

# Constraints:

# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 107
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 105 calls will be made to set and get.

# Solution

# User Solution copied, main logic is same, the way of applying binary search
# is bit different
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dic[key]
        n = len(arr)
        
        left = 0
        right = n
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid
        
        return "" if right == 0 else arr[right - 1][1]
# My Solution
# class TimeMap:

#     def __init__(self):
#         self.timeStampValues = {}
#         self.keyTimeStamp = {}
        

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key in self.keyTimeStamp:
#             self.keyTimeStamp[key].append(timestamp)
#         else:
#             self.keyTimeStamp[key] = [timestamp]
        
#         self.timeStampValues[timestamp] = value

#     def get(self, key: str, timestamp: int) -> str:
#         low = 0
#         if key in self.keyTimeStamp:
#           high = len(self.keyTimeStamp[key])-1
#         else:
#           return ""
#         while low<=high:
#             mid = (low+high)//2
#             if self.keyTimeStamp[key][mid]>timestamp:
#                 high = mid-1
#                 if high<low and high<0:
#                     return ""
#             elif self.keyTimeStamp[key][mid]<timestamp:
#                 low = mid+1
#             else:
#                 return self.timeStampValues[timestamp]
        
        
#         return self.timeStampValues[self.keyTimeStamp[key][low-1]]

if __name__ == "__main__":
    obj = TimeMap()
    obj.set("foo", "bar", 1)
    obj.set("foo", "bar2", 4)
    print(obj.get("foo", 4))