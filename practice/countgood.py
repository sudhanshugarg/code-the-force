# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #do pre-order dfs. and keep track

        count_good = [0]
        def dfs(node: TreeNode, curr_max: int, count: List[int]):
            if node.val >= curr_max:
                count[0] += 1
                curr_max = node.val            

            if node.left is not None:
                dfs(node.left, curr_max, count)
            
            if node.right is not None:
                dfs(node.right, curr_max, count)

        dfs(root, root.val, count_good)
        return count_good[0]
