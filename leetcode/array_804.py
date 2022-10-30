class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # 转换为哈希表
        hashtable = dict(zip(letter,morse))
        #print(hashtable)

        def letter2morse(lst):
            # 将列表中的元素转化为莫斯代码
            res = []
            for i in lst:
                #print(i)
                res.append(hashtable.get(i))
            #print("".join(res))
            return "".join(res)
        #letter2morse(words[0])
        # 存储变为莫斯代码的列表
        res = []
        for i in range(len(words)):
            res.append(letter2morse(words[i]))
        print(res)
        print(len(set(res)))

words = ["gin","zen","gig","msg"]
words = ["a"]
obj = Solution().uniqueMorseRepresentations(words)
