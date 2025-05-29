class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        l_wall = r_wall = 0
        max_left = [0] * n
        max_right = [0] * n
        for i in range(n):
            j = -i - 1
            max_left[i] = l_wall
            max_right[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
        summ = 0
        for i in range(n):
            pot = min(l_wall[i], r_wall[i])
            summ += max(0, pot - height[i])
        return summ
    
    #time: O(n)  space: O(n