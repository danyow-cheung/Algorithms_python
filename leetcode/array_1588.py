class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        -每一个距离增肌
        -每3个距离增加
        -最后全加一起
        """
        res = 0 
        
        def loop(arr):
            res = 0
            for i in arr:
                res+=i 
            return res 
        # example2 
        if len(arr)<3:
            for i in arr:
                res += i 
        
        
        for i in range(len(arr)):
            res += arr[i]
            # 15

        for i in range(3):
            print(f"{i}---{arr[i:i+3]}")

            res += loop(arr[i:i+3])

                
        for i in arr:
            res+=i     
        print(res)

        
arr = [1,4,2,5,3]
# arr = [1,2]
obj = Solution().sumOddLengthSubarrays(arr)