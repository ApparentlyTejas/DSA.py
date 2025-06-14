class Solution:
    def pathSum(self, root: Optional[TreeNode] , targetSum: int) -> bool:
        def hasSum(root , cur_sum):
            if not root:
                return False
            
            cur_sum += root.val

            if not root.right and not root.left:
                return cur_sum == targetSum
            
            return hasSum(root.left , cur_sum) or hasSum(root.right , cur_sum)
        
        return hasSum(root , 0)
    
    # Time: O(n)
    # Space: O(h)  or O(n) in worst case