class TrieNode:

    def __init__(self, ):
        self.children = [None] * 26
        self.isEow = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        return TrieNode()

    def _charToIndex(self, ch):

        return ord(ch) - ord('a')

    def insert(self, key):

        pcrawl = self.root

        for level in range(len(key)):

            idx = self._charToIndex(key[level])

            if not pcrawl.children[idx]:
                pcrawl.children[idx] = self.getNode()
            pcrawl = pcrawl.children[idx]
        pcrawl.isEow = True
        pcrawl.word = key

    def search(self, key):
        pcrawl = self.root

        for level in range(len(key)):

            idx = self._charToIndex(key[level])

            if not pcrawl.children[idx]:
                return False
            pcrawl = pcrawl.children[idx]
        return pcrawl != None and pcrawl.isEow

    def isLeafNode(self, node):
        return node.isEow != False

    def printTrie(self, root):
        if self.isLeafNode(root):
            string = root.word
            print(string)
        for i in range(26):
            if root.children[i]:
                self.printTrie(root.children[i])


if __name__ == "__main__":
    keys = ["the", "a", "there", "answer", "any", "by", "their"]
    output = ["not present", "present"]
    t = Trie()

    for key in keys:
        t.insert(key)

    print("{}---{}".format("there", output[t.search("there")]))
    print("{}---{}".format("the", output[t.search("the")]))
    s = []
    t.printTrie(t.root)
