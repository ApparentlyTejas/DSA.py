class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        sol , res = [] , []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return 
            
            #backtrack left ie: not picking num[i]

            backtrack(i + 1)

            #backtrack right

            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)
        return res
    
# Time: O(2^n)
# Space: O(n)