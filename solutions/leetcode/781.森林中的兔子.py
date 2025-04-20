#
# @lc app=leetcode.cn id=781 lang=python3
#
# [781] 森林中的兔子
#

# @lc code=start
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()

        tot, cd = 0, 1
        for i, num in enumerate(answers):
            if i == 0 or num != answers[i - 1]:
                cd = num + 1
                tot += num + 1
                continue
            cd = max(0, cd - 1)
            if cd == 0:
                tot += num + 1
                cd = num + 1
                
        return tot
        
# @lc code=end

