class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        
        # m表示有多少個數組
        :type m: int
        # n代表一數組裡面塞多少個元素
        :type n: int
        
        :rtype: List[List[int]]
        """
        res = []
        # 判錯處理
        if m*n != len(original) :
            print(res) 

        for i in range(len(original)):
            res.append(original[:n])
            del original[:n]
            i+= n 
            if len(res)==m:
                break

        print(res)
        #return res 

            
original = [1,2,3,4]
m = 2
n = 2
obj = Solution().construct2DArray(original,m,n)
