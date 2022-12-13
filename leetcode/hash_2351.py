class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        hash = {}
        for i in range(len(s)):

            if s[i] not in hash:
                hash[s[i]] = 1
            elif hash[s[i]]>=1:
                hash[s[i]]+=1
            if hash[s[i]]==2:

                print(s[i])
                return s[i]
                break

        print(hash)
        return None


s = "abccbaacz"
obj = Solution().repeatedCharacter(s)