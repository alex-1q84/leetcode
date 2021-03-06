package me.changhai.leetcode;

import java.util.*;

/**
 * Definition for binary tree
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class SymmetricTree {
    /**
     *      1
     *     / \
     *    2   2
     *   / \ / \
     *  3  4 4  3
     *  OJ's Binary Tree Serialization
     *  {1, 2, 2, 3, 4, 4, 3}
     *
     *     1
     *    / \
     *   2   3
     *      /
     *     4
     *      \
     *       5
     *  OJ's Binary Tree Serialization
     *  {1,2,3,#,#,4,#,#,5}
     */
    public List<String> serializeToOJList(TreeNode root) {
        ArrayList<String> flattenNodesVal = new ArrayList<String>();
        flattenNodesVal.add(String.valueOf(root.val));
        if(root.left == null){
            flattenNodesVal.add("#");
        }
        if(root.right == null){
            flattenNodesVal.add("#");
        }

        return null;
    }

    public boolean isSymmetric(TreeNode root) {

        return false;
    }
}
