class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        ans = 0
        cur_word = "a"

        # 初始化为a
        if word[0]=='a':
            ans +=1

        # 旋转多少度找到的累加
        for i in word:
            move = min(abs(ord(cur_word) - ord(i)),abs(abs(ord(cur_word) - ord(i))-26))
            ans +=move+1
            cur_word = i

        print(ans)
        return ans
word = "zjpc"
obj = Solution().minTimeToType(word)