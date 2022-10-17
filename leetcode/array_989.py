from platform import java_ver


class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        str_num = ""
        for i in num:
            str_num += str(i)
        sum = int(str_num)+k 
        sum = str(sum)
        res = [int(i) for i in sum]
        return res         
nums = [2,7,4]
k = 181
obj = Solution().addToArrayForm(nums,k)