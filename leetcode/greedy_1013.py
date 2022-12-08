class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # why we need to use this?
        expecteed = sum(arr)
        if expecteed % 3 != 0:
            return False

        total = 0
        count = 0
        for i in arr:
            total += i
            if total == expecteed // 3:
                count += 1
                total = 0

        return count >= 3


arr = [0,2,1,-6,6,-7,9,1,2,0,1]
arr = [3,3,6,5,-2,2,5,1,-9,4]
arr = [0,0,0,0]
obj = Solution().canThreePartsEqualSum(arr)