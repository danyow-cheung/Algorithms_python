class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # for  i in range(len(arr)):
            # print(arr[i],bin(arr[i])[2:])
        sorted(arr,key = lambda x: [bin(x).count('1'),x])

        print(arr)

        
arr = [0,1,2,3,4,5,6,7,8]
obj = Solution().sortByBits(arr)