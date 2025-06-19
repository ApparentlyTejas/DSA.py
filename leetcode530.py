class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = [float('inf')]
        prev = [None] 

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)

            if prev[0] is not None:
                min_diff[0] = min( min_diff[0] , node.val - prev[0])

            prev[0] = node.val

            dfs(node.right)

        dfs(root)

        return min_diff[0]
    
# Time: O(n)
# Space: O(n)