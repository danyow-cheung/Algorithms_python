class TreiNode:
    def __init__(self):
        self.children = {}
        self.end_char = False 

class Trie(object):

    '''
    Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

    请你实现 Trie 类：

    Trie() 初始化前缀树对象。
    void insert(String word) 向前缀树中插入字符串 word 。
    boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
    boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
    '''
    def __init__(self):
        '''
        https://leetcode.com/problems/implement-trie-prefix-tree/solutions/2935951/beats-95-codedominar-solution/
        Dictionary
        '''
        self.root = TreiNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root 
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreiNode()
            curr = curr.children[c]
        curr.end_char = True

        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root 
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end_char

        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr =self.root 
        for c in prefix:
            if c not in curr.children:
                return False 
            curr = curr.children[c]
        return True
    
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
