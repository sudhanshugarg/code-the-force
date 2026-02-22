# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(level: int, root: Optional[TreeNode], result: List[List[int]]):
            if root is None:
                return
            
            #should do pre-order so that root elements are present.
            if len(result) <= level:
                result.append([])

            dfs(level+1, root.left, result)
            dfs(level+1, root.right, result)
            result[level].append(root.val)

        result = []
        dfs(0, root, result)
        return result

"""
thoughts
ans1: bfs. O(n) time, O(n) queue space
ans2: dfs. insert each node pre/in/post-order into correct level
which order? doesn't matter. O(n) time, O(1) space (excluding the space for the actual answer)
"""