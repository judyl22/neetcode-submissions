class TreeNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        
        def dfs(word, root):
            curr = root
            for i, c in enumerate(word):
                if c == '.':
                    for child in curr.children.values():
                        new_word = word[i+1:]
                        if dfs(new_word, child):
                            return True
                    return False
                elif c not in curr.children:
                    return False
                else:
                    curr = curr.children[c]
            return curr.end

        return dfs(word, self.root)
        
