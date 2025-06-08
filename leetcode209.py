class Solution:
    def minSubArrayLength(self, target: int, nums: list[int]) -> int:
        min_len = float('inf')
        l = 0
        n = len(nums)
        summ = 0
        
        for r in range(n):
            summ += nums[r]

            while summ >= target:
                min_len = min(min_len , r - l + 1)
                summ -= nums[l]
                l += 1
        return min_len if min_len < float('inf') else 0
    
#time: O(n)     space: O(1)