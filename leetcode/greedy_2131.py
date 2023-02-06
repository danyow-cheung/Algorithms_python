class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        m = len(words)

        import collections
        # 每個元素的長度都是2，回文字串只要滿足每個都是偶數的平方就可以
        res = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i]==words[j][::-1]:
                    res.append(words[i])
                    res.append(words[j])

        print(res)
        ans = sum(len(i) for i in res)

        if m%2==0:
            print(ans)

            return ans
        elif res==[]:
            return 2 

        else:
            # 先找到這個元素
            left= [i for i in words if i not in res ]
            print("left",left)

            # 判斷這個字符是不是回文
            if left==left[::-1]:
                print(ans+2)

                return ans+2
words = ["lc","cl","gg"]
words = ["ab","ty","yt","lc","cl","ab"]
words = ["cc","ll","xx"]

obj = Solution().longestPalindrome(words)