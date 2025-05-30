class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stk = []
        answer = [0] * n
        for i, t in enumerate(temperatures):
            while stk and stk[-1][0] < t:
                stk_t , stk_i = stk.pop()
                answer[stk_i] = i - stk_i
            stk.append((t, i))
        return answer
    
#time: O(n)   space: O(n)