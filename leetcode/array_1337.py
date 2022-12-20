class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        old_mat = mat.copy()
        mat.sort(key=lambda x:x.count(1))
        for i in range(len(mat)):
            print(mat[i],old_mat.index(mat[i]))
            idx = old_mat.index(mat[i])
            if idx == old_mat.index(mat[i-1]):
                print('equal',mat[i])
        # ans = []
        # for i in range(k):
        #     print(old_mat.index(mat[i]))
        #     ans.append(old_mat.index(mat[i]))
        # print(ans)
        # return  ans
    def kWeakestRows_leetcode(self,mat,k):
        res = []
        for i in mat:
            res.append(sum(i))
        print(res)
        if len(res)==0:
            return [0]
        ans = []
        for j in sorted(res):

            x = res.index(j)
            # 存儲下標
            ans.append(x)
            #  去除相同元素的影響
            res[x]=-1
            print(j, x, res)
        return ans[:k]



mat = [
     [1,1,0,0,0],
     [1,1,1,1,0],
     [1,0,0,0,0],
     [1,1,0,0,0],
     [1,1,1,1,1]
 ]
k = 3

obj = Solution().kWeakestRows_leetcode(mat,k)