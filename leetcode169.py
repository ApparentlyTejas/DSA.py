class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        ans = -1
        for num in nums:
            if count == 0:
                ans = nums
            if ans == nums:
                count += 1
            else:
                count -= 1
        return ans
    
#time: O(n)
#space: O(1)