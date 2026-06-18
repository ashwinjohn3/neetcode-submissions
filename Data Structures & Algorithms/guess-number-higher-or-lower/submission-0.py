# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
import random

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n 
        answer = None
        mid = (l+r)//2
        while answer != 0:
            mid = (l+r)//2
            answer = guess(mid)

            if answer > 0:
                l = mid + 1
            elif answer < 0: 
                r = mid - 1
     
        return mid 

