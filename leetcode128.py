class Solution:
    def longestConsecutive(self, nums: list[int])-> int:
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:
                next_num = num + 1
                length = 1
                while next_num in s:
                    length += 1
                    next_num += 1
                longest = max(length, longest)
        return longest
    #time : O(n)
    #space: O(n)