import collections


class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        dict ={'a':0,'e':0,'i':0,'o':0,'u':0}
        # 构建哈希表
        for i in word:
            if i in dict:
                dict[i]+=1

        print('dict = ',dict)
        ans = 1
        # 缺少部分元素
        if min(dict.values())==0:
            ans = 0
            return ans

        for value in dict.values():
            ans*=value
        print('ans,len(word)',ans,len(word))

        return ans

word = 'aeiouu'
# word = "unicornarihan"
word = "cuaieuouac"
obj = Solution().countVowelSubstrings(word)