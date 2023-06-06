"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.l=[]
        self.pre(root)
        return self.l
    def pre(self,root):
        if root is None:
            return
        self.l.append(root.val)
        for i in root.children:
            self.pre(i)
