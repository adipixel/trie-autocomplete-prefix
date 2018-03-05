# Trie API
Simple Trie data structure API usually used for fast reTRIEval of words for autocomplete.

### Import API
```
from trie import *
```

### Create a Trie
```
myTrie = Trie()
```

### Add word to Trie
```
myTrie.addWord("all")
myTrie.addWord("also")
myTrie.addWord("already")
```

### Retrive words for a prefix

```
prefix = "al"
result = myTrie.getWords(prefix)
```
Results:
This returns the children and the word count (number, dict) pair
```
result -> 3, {'l': <>, 's': <>, 'r': <>}
```
