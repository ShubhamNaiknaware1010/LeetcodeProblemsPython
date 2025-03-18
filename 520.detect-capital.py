#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for i in range(len(word)):
            if word[i].upper() == word[i]:
                count += 1
        if count == len(word) or count == 0 or (count == 1 and word[0] == word[0].upper()):
            return True
        return False
# @lc code=end

