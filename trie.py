class TrieNode:
    def __init__(self):
        self.words = 0
        self.prefixes = 0
        self.children = dict()
        self.validFlag = False

    # adds letter to the Trie tree
    # returns the newly added node
    def addLetter(self, letter, validFlag):
        # TrieNode already exists
        if letter in self.children:
            self.words += 1
            return(self.children[letter])

        # create a trie node and link it
        self.children[letter] = TrieNode()
        if not validFlag:
            self.validFlag = validFlag
        self.words += 1
        return(self.children[letter])



class Trie:
    # global variable
    root = None

    # initialize trie's root node
    def __init__(self):
        self.root = TrieNode()

    # adds WORD to trie
    def addWord(self, word):
        node = self.root
        for i in range(len(word)):
            if i == len(word)-1:
                # adds letter to trie tree
                node = node.addLetter(word[i], True) # last char of the word
            else:
                # adds letter to trie tree
                node = node.addLetter(word[i], False)

    # iterates in search of given prefix
    # returns word count and children
    def getChildren(self, prefix):
        node = self.root
        for x in prefix:
            if x in node.children:
                node = node.children[x]
            else:
                return -1, None
        return node.words, node.children


# driver function
def main():
    t = Trie()
    t.addWord("tree")
    t.addWord("trie")
    t.addWord("algo")
    t.addWord("assoc")
    t.addWord("all")
    t.addWord("also")

    prefix = "al"
    words, children = t.getChildren(prefix) # words: 3, children: g, l, s
    print(words, children)


main()
