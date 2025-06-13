class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def same(root1, root2):
            if not root1 and not root2:
                return True
            
            if (root1 and not root2) or (root2 and not root1):
                return False
            
            if root1.val != root2.val:
                return False
            
            return same(root1.left , root2.right) and same(root1.right , root2.left)
        
        return same(root , root)
# Time: O(n)
# Space: O(h)