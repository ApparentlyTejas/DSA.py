from collections import deque
class Solution:
    def levelOrder(self , root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []
        
        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(level)

        return ans
    
# Time: O(n)
# Space: O(n)