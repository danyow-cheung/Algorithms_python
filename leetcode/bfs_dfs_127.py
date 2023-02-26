from collections import defaultdict,deque

class Solution(object):
    def __init__(self):
        
        self.length = 0 
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self,queue,visited,others_visited):
        queue_size = len(queue)
        for _ in range(queue_size):
            current_word = queue.popleft()
            for i in range(self.length):
                intermediate_word = current_word[:i]+"*"+current_word[i+1:]
                for word in self.all_combo_dict[intermediate_word]:
                    if word in others_visited:
                        return visited[current_word]+others_visited[word]
                    if word not in visited:
                        visited[word]=visited[current_word]+ 1
                        queue.append(word)
        return None
    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        https://leetcode.com/problems/word-ladder/editorial/
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0 
        for word in wordList:
            for i in range(self.length):
                self.all_combo_dict[word[:i]+'*'+word[i+1:]].append(word)
        queue_begin = deque([beginWord])
        queue_end = deque([endWord])

        visited_begin  = {beginWord:1}
        visited_end = {endWord:1}
        ans = None
        while queue_begin and queue_end:
            if len(queue_begin)<=len(queue_end):
                ans = self.visitWordNode(queue_begin,visited_begin,visited_end)
            else:
                ans = self.visitWordNode(queue_end,visited_end,visited_end)
            if ans:
                return ans 
        return  0
    

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
obj = Solution().ladderLength(beginWord,endWord,wordList)