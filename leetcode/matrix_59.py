class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==1:
            return [[1]]

        res = [[-1 for i in range(n) ]for i in range(n)]
        print(res)

        total = n**2 
        print(total)
         
        for i in range(1,n+1):
            print("i",i)

            # 1-2-3
            res[0][i-1]=i 
            #3-4-5
            res[i-1][n-1]=i+2
            # 5-6-7
            # res[-1][n-1]=i+3

        print(res)
        
    def generateMatrix_leetcode(self, n):
        nums = [[0]* n for _ in range(n)]
        # 起始點
        startx = 0 
        starty = 0
        # 迭代次數
        loop = n//2 
        mid = n//2
        # 計數 
        count = 1 
        for offset in range(1,loop+1): # 每循環一層偏移量+1，偏移量從1開始
            for i in range(starty,n-offset):# 從左到右，左閉右開
                nums[startx][i]= count 
                count += 1 
            for i in range(startx,n-offset):# 從上到下
                nums[i][n-offset]=count
                count +=1 
            for i in range(n-offset,starty,-1):# 從右到左
                nums[n-offset][i]=count 
                count+=1 
            for i in range(n-offset,startx,-1):# 從下到上
                nums[i][starty]=count 
                count +=  1
            startx +=  1 # 更新起始點
            starty +=  1 
        if n%2!=0:
            nums[mid][mid]=count # n為奇數，填充中心點
            
        return nums

n = 3 
# n = 2
# n =1 
obj = Solution().generateMatrix(n)