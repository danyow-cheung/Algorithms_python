import collections


class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        ans =[]
        print(min(count.keys()),count[min(count.keys())])
        print(count.most_common()[0][1])
        while count.most_common()[0][1] !=0:
            for i in range(ord('a'),ord('z')+1):
                # print(i,type(i))
                if count[chr(i)] :
                    # print(chr(i))
                    ans.append(chr(i))
                    count[chr(i)]-=1
            for i in reversed(range(ord('a'),ord('z')+1,)):

                if count[chr(i)]:
                    # print(chr(i))
                    ans.append(chr(i))
                    count[chr(i)]-=1
        # # print(count)
        
        print ("".join(ans))
        return "".join(ans)

s = "aaaabbbbcccc"
s = "leetcode"
obj = Solution().sortString(s)