"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.l=[]
        self.post(root)
        return self.l

    def post(self,root):
        if root is None:
            return
        for i in root.children:
            self.post(i)        
        self.l.append(root.val)
