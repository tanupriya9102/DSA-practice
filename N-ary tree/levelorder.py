"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.l=[]
        self.level(root)
        return self.l
    
    def level(self,root):
        
        # result = []
        if root is None:
            return
        queue = [root]
        next_queue = []
        level = []
        
        while len(queue)>0:
            for root in queue:
                level.append(root.val)
                for i in root.children:
                    if i:
                        next_queue.append(i)               
            self.l.append(level)
            level = []
            queue = next_queue
            next_queue = []
        

