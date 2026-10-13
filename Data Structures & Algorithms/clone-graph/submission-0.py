"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        new_nodes_dict = {}
        
        def dfs(node):
            if node.val in new_nodes_dict:
                return new_nodes_dict[node.val]
            curr_node = Node(node.val)
            new_nodes_dict[node.val] = curr_node
            for neigh in node.neighbors:
                curr_node.neighbors.append(dfs(neigh))
            return curr_node
        
        return dfs(node)