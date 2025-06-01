class Solution:
    def findMin(self, nums: list[int])-> int:
        n = len(nums)
        r = n - 1
        l = 0
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
    
#time: O(log n)   space: O(1)
    