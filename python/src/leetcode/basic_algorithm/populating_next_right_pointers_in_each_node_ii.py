# 202203221459
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/
# 给定一个二叉树
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        if root.left and root.right:
            root.left.next = root.right
        if root.left and not root.right:
            root.left.next = get_next(root.next)
        if root.right:
            root.right.next = get_next(root.next)
        self.connect(root.right)
        self.connect(root.left)
        return root


def get_next(root: 'Node'):
    if not root:
        return None
    if root.left:
        return root.left
    elif root.right:
        return root.right
    else:
        return get_next(root.next)
