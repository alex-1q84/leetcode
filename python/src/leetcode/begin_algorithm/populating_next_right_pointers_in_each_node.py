# 202203011725
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # 广度优先
        if root is None or root.left is None:
            return root
        root.left.next = root.right
        # 连接左右节点的右子节点和左子节点
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
