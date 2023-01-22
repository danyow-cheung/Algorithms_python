class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        coor = []

        def loop(sr,sc):
            if image[sr][sc-1]==image[sr][sc]:
                image[sr][sc-1] = color
                coor.append([sr,sc-1])
            if image[sr][sc + 1] == image[sr][sc]:
                image[sr][sc + 1] = color
                coor.append([sr, sc + 1])
            if image[sr-1][sc] == image[sr][sc]:
                image[sr-1][sc]= color
                coor.append([sr-1,sc])
            if image[sr+1][sc] == image[sr][sc]:
                image[sr+1][sc] = color
                coor.append([sr+1, sc])
            # print(image)
            return image

        image= loop(image,sr,sc)
        print(image)
        # print(coor)
        for x,y in coor:
            # print(x,y)
            image = loop(image,x,y)
        print(image)
        # # 上
        # print(image[sr][sc-1])
        # # 下
        # print(image[sr][sc+1])
        # # 左
        # print(image[sr-1][sc])
        # # 右
        # print(image[sr+1][sc])
        # return image

    def floodFill_leetcode(self, image, sr, sc, newColor):
        R = len(image)
        C = len(image[0])
        color = image[sr][sc]
        if newColor ==color:
            return image
        def dfs(r,c):
            if image[r][c]==color:
                image[r][c]==newColor
                if r>=1:dfs(r-1,c)
                if r+1<R:dfs(r+1,c)
                if c>=1:dfs(r,c-1)
                if c+1<C:dfs(r,c+1)
        dfs(sr,sc)
        return image

image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
obj = Solution().floodFill(image,sr,sc,color)