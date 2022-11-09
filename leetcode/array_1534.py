class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        res = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                        res +=1
        print(res)
arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3

arr = [1,1,2,2,3]
a = 0
b = 0
c = 1
obj = Solution().countGoodTriplets(arr,a,b,c)