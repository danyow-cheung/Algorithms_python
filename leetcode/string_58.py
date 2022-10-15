class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        # 轉換成list
        s = s.strip()
        
        s = s.split(" ")
        return len(s[-1])
        
        
s = "   fly me   to   the moon  "
# s = "luffy is still joyboy"
# s = "hello world"
obj = Solution().lengthOfLastWord(s)