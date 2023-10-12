import math
import os
import random
import re
import sys

#
# Complete the 'beautifulStrings' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING s as parameter.
#

# def beautifulStrings(s):
    # Write your code here
    # abdde
    # abc

    # aaaa
    # 1111

    # uniqStrings = {}
    # counter = 0
    # for i in range(0,len(s)):
    #     if(i != len(s)-1):
    #         for j in range(i+1,len(s)):
    #             if((s[:i]+s[i+1:j]+s[j+1:len(s)]) not in uniqStrings):
    #                 uniqStrings[(s[:i]+s[i+1:j]+s[j+1:len(s)])] = 0
    #                 counter += 1
    # return counter

def min_operations_to_beautiful(s):
    # ops = 0
    # i = 0
    # while i < len(s) - 1:
    #     diff = ord(s[i]) - ord(s[i+1])
    #     if diff in [0, 1, -1]:
    #         ops += 1
    #         i += 2  # skip the next character
    #     else:
    #         i += 1
    # return ops

    ops  = 0
    i = 0
    while i < len(s) - 1:
        diff = ord(s[i]) - ord(s[i+1])
        if diff in [0,1,-1]:
            ops += 1
            i += 2
        else:
            i += 1
    
    return ops

if __name__ == '__main__':
    s = "bartqa"
    # aaaaa
    # 10101
    # aabc
    # 111
    print(min_operations_to_beautiful(s))
