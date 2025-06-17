from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        avg = []
        queue = deque()
        queue.append(root)

        while queue:
            summ = 0
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()
                summ += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avg.append(summ / n)
        return avg
    
# Time: O(n)
# Space: O(n)