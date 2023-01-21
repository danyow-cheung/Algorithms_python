class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        temp =  0
        n  = len(bits)
        while i<n:
            if bits[i]==0:
                temp =0
                i+=1
            else:
                temp = 1
                i+=2
        if temp==0:
            return True
        else:
            return False

bits = [1,0,0]
obj = Solution().isOneBitCharacter(bits)