class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ans= address.replace('.','[.]')
        print(ans)

        print(address)
address = "1.1.1.1"
obj = Solution().defangIPaddr(address)