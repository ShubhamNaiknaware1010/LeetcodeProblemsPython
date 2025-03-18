#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        sqrt = int(num ** 0.5)
        sum = 1
        for i in range(2,sqrt + 1):
            if num  % i == 0:
                if i == num:
                    sum -= i 
                sum += i  + (num // i)
        return  sum == num
        
# @lc code=end

