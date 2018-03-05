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
            if validFlag:
                self.children[letter].validFlag = validFlag
            return(self.children[letter])

        # create a trie node and link it
        self.children[letter] = TrieNode()
        self.children[letter].validFlag = validFlag
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
    def getWords(self, prefix):
        node = self.root
        curWord = ""
        childWords = [] # word list to return

        # iterate to the prefix in the trie
        for x in prefix:
            curWord += x
            if x in node.children:
                node = node.children[x]
            else:
                return 0, None

        # merging retrived list
        childWords += self.getCompleteWordList(node, curWord)

        if node.validFlag:
            return node.words+1, childWords
        else:
            return node.words, childWords

    def getCompleteWordList(self, curNode, curWord):
        node = curNode
        wordList = []
        if node.validFlag:
            wordList.append(curWord)
        for child in node.children:
            wordList += self.getCompleteWordList(node.children[child], curWord+child)
        return wordList
