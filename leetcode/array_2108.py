class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        找出数组中的第一个回文字符串
        """
        def check(s):
            left = 0
            right = len(s) - 1
            res = 0
            while left < len(s):
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                    if left == right:
                        res = 1
                else:
                    break
            return res

        for i in words:
            # print(i)
            if check(i)==1:
                print(i)
                # return i
                # break
                # return i
            else:
                print ("")

        def leetcode(self,words):
            for i in words:
                if i == i[-1::-1]:
                    return i
            return ""

words = ["abc","car","ada","racecar","cool"]
# words = ["notapalindrome","racecar"]
obj = Solution().firstPalindrome(words)

