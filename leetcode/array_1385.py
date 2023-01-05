class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr1)
        ans=  0
        for i in range(len(arr1)):
            cur = 0
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<= d:
                    print(arr1[i], arr2[j])
                    cur += 1
            if cur!= 0:
                ans +=1
        print(n - ans)

        return n - ans
arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2

arr1 = [1,4,2,3]
arr2 = [-4,-3,6,10,20,30]
d = 3

arr1 = [2,1,100,3]
arr2 = [-5,-2,10,-3,7]
d = 6

obj = Solution().findTheDistanceValue(arr1,arr2,d)