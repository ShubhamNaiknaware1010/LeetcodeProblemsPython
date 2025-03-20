#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = [0,0]
        for bill in bills:
            if bill == 5:
                cash[0] += 1
            elif bill == 10 and cash[0] > 0:
                cash[1] += 1
                cash[0] -= 1
            elif bill == 20 and (cash[0] >= 3 or (cash[0] > 0 and cash[1] > 0)):
                if cash[1] > 0:
                     cash[1] -= 1
                     cash[0] -= 1
                else:
                    cash[0] -= 3
            else:
                return False
        return True 

# @lc code=end

