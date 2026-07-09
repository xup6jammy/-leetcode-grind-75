"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Time: O(n)
Space: O(n)
"""


class Solution:
    def twoSum(self, nums, target):
        # 創建一個dict
        seen = {}
        # 將傳入的list拆成 index 跟 數字
        for i, num in enumerate(nums):
            # 我要找的數字 - 數字 = 對應的被減數字
            complement = target - num
            # 檢查被減的數字是否存在dict中
            if complement in seen:
                # 有就返回 被減數字的value , 當下的index 
                return [seen[complement], i]
            # 如果沒有就將當下的位置儲存在dict{數字:座標}
            seen[num] = i
        # 如果都找不到就返回空陣列 
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
