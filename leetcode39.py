class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans , sol = [], []
        nums = candidates
        n = len(nums)

        def backtrack(i , cur_sum):
            if cur_sum == target:
                ans.append(sol[:])
                return
            
            if cur_sum > target or i == n:
                return
            
            backtrack(i+ 1 , cur_sum)

            sol.append(nums[i])
            backtrack( i , cur_sum + nums[i])
            sol.pop()

            backtrack(0 , 0)
            return ans
        
# Time: O(n ** t)
# Space: O(n)