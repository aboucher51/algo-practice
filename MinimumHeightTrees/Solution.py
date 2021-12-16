class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        leaves = []
        
        for i in range(n):
            if(len(neighbors[i]) == 1):
                leaves.append(i)
                    
        remaining_nodes = n
        while remaining_nodes > 2 :
            remaining_nodes -= len(leaves)
            new_leaves = []
            
            while leaves:
                leaf = leaves.pop()
                # remove the only neighbor remaining for the current leaf
                neighbor = neighbors[leaf].pop()
                # remove that neighbor's edge-reference to the current leaf
                neighbors[neighbor].remove(leaf)
                # if that neighbor is a new leaf themself, then add to new leaves
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
                    
            leaves = new_leaves
        return leaves