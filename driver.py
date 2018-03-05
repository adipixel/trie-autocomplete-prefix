from trie import *

# driver function
def main():
    t = Trie()
    # adding word to trie
    t.addWord("tree")
    t.addWord("trie")
    t.addWord("algo")
    t.addWord("assoc")
    t.addWord("all")
    t.addWord("also")

    prefix = "al"
    # retriveing word
    words, children = t.getChildren(prefix) # words: 3, children: g, l, s
    print(words, children)


main()
