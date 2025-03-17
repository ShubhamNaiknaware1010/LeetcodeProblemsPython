#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        dp = [0,1]
        for i in range(2,n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]
        
# @lc code=end

