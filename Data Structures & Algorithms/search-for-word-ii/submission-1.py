class Node:
    def __init__(self):
        self.children = {}
        self.end_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end_word = True
    
    def check(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end_word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()
        for word in words:
            trie.insert(word)

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(r, c, curr, next_index):
            if curr.end_word:
                chars = []
                for i in range(next_index):
                    chars.append(path_dict[i])
                found.add("".join(chars))

            for dr, dc in directions:
                newr = r + dr
                newc = c + dc
                if min(newr, newc) < 0 or newr >= row_num or newc >= col_num or (newr, newc) in visited:
                    continue
                next_char = board[newr][newc]
                if next_char in curr.children:
                    next_node = curr.children[next_char]
                    visited.add((newr, newc))
                    path_dict[next_index] = next_char
                    dfs(newr, newc, next_node, next_index + 1)
                    visited.remove((newr, newc))
                    path_dict.pop(next_index)

        row_num = len(board)
        col_num = len(board[0])
        found = set()
        root = trie.root
        for r in range(row_num):
            for c in range(col_num):
                char = board[r][c]
                if char in root.children:
                    visited = set()
                    visited.add((r, c))
                    path_dict = {}
                    path_dict[0] = char
                    dfs(r, c, root.children[char], 1)
        return list(found)