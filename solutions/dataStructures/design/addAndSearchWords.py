class WordDictionary:

    def __init__(self):
        # We will represent this as a list of arrays
        # Intuitively, each level of the tree is a potential path or character choice from a-z
        # isEndOfWord is a flag, so we can still detect end of words for searching or adding with same prefix
        self.children = [None] * 26
        self.isEndOfWord = False


    def addWord(self, word: str) -> None:
        # Adds a word into our data structure by parsing through the word string
        # and for each character we check if it exists, if not create a new word dictionary DS or path
        # Set end of word flag to true
        curr = self
        for c in word:
            if curr.children[ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = WordDictionary()
            curr = curr.children[ord(c) - ord('a')]
        
        curr.isEndOfWord = True


    def search(self, word: str) -> bool:
        # Searches for a word and returns True if found, false otherwise
        # Parse through the word string and checks layer by layer if all of the characters exist
        # Allows for '.' which can represent any character through recursing through all possible paths at current level
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children:
                    if ch != None and ch.search(word[i + 1:]): return True
                return False
            
            if curr.children[ord(c) - ord('a')] == None: return False
            curr = curr.children[ord(c) - ord('a')]

        return curr != None and curr.isEndOfWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


"""
Solution with using dictionary and DFS for search to optimize memory and runtime

class WordDictionary:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.isEndOfWord

            c = word[index]
            if c == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c], index + 1)

        return dfs(self, 0)

"""