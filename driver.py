from trie import *

# driver function
def main():
    t = Trie()
    t.addWord("tree")
    t.addWord("trie")
    t.addWord("algo")
    t.addWord("assoc")
    t.addWord("all")
    t.addWord("also")
    t.addWord("al")
    t.addWord("algorithm")
    t.addWord("algorithms")

    prefix = "al"
    words, children = t.getWords(prefix) # 6 ['al', 'algo', 'algorithm', 'algorithms', 'all', 'also']
    print(words, children)


main()
