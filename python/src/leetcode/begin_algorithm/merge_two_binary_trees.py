# 202203011636
# https://leetcode-cn.com/problems/merge-two-binary-trees/
# 给你两棵二叉树： root1 和 root2 。
# 想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。 你需要将这两棵树合并成一棵新二叉树。
# 合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；
# 否则，不为 null 的节点将直接作为新二叉树的节点。
# 返回合并后的二叉树。
# 注意: 合并过程必须从两个树的根节点开始。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 深度优先
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        else:
            return TreeNode(root1.val + root2.val,
                            self.mergeTrees(root1.left, root2.left),
                            self.mergeTrees(root1.right, root2.right))
