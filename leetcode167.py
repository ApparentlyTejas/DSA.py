class Solution:
    def twoSum(self, numbers:list[int], target: int) -> list[int]:
        n = len(numbers)
        l =0 
        r= n-1
        while l < r:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l+1, r+1]
            elif summ > target:
                r -= 1
            else:
                l += 1
#time: O(n) space: O(1)