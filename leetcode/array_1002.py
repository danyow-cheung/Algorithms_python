class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        查找每个字符中的都出现的共用字符，并以数组形式返回
        """
        import  collections
        counts = collections.Counter(words[0])

        for i in words[1:]:
            #&= 求集合交集？
            counts &= collections.Counter(i)
        # 不加list的话，返回是内置数据结构，得不到元素
        print(list(counts.elements()))

words = ['bella','label','roller']
# words =["cool","lock","cook"]
obj = Solution().commonChars(words)
