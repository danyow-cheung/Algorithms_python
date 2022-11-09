class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        for i in image:
            cur = []
            for j in i[::-1]:
                if j == 0 :
                    j=1
                elif j == 1:
                    j=0
                cur.append(j)
            print("直接切片转换的", i[::-1],"更改数字之后的",cur)
            # print(cur)
            ans.append(cur)
        print(ans)

image = [[1,1,0],[1,0,1],[0,0,0]]
obj = Solution().flipAndInvertImage(image)