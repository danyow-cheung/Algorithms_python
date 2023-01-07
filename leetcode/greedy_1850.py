class Solution(object):

    def getMinSwaps(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: int
        查找給定字符串的下一個排列 k 次。

        嘗試將每個元素移動到正確的位置併計算步數。
        """
        right = len(num)-1
        lst = []

        while 1:

            new_lst = num[:right-1]

            print(new_lst)
            break


    def getMinSwaps_leetcode_v1(self,num,k):
        def next_perm(num):
            i = n-1
            while i>0 and num[i-1]>= num[i]:
                i-=1
            j = i
            while j<n and num[i-1]<num[j]:
                j+=1
            num[i-1],num[j-1] = num[j-1],num[i-1]
            num[i:] =num[i:][::-1]
            return  num
        n = len(num)
        next_k_num = list(num)
        for _ in range(k):
            next_k_num = next_perm(next_k_num)
        ans = 0
        num = list(num)
        for i in range(n):
            j = i
            while j<n and next_k_num[i]!=num[j]:
                j+=1
            ans += j-i
            num[i:j+1] = [num[j]]+num[i:j]
        print(ans)

    def getMinSwaps_leetcode_v2(self, num, k):
        num = list(num)
        orig = num.copy()
        # print(num,orig)

        for _ in range(k):
            for i in reversed(range(len(num)-1)):
                print(num[i])
                if num[i]<num[i+1]:
                    ii = i+1
                    while ii<len(num) and num[i]<num[ii]:
                        ii+=1

                    num[i],num[ii-1] = num[ii-1],num[i]
                    lo,hi = i+1,len(num)-1
                    while lo<hi:
                        num[lo],num[hi] = num[hi],num[lo]
                        lo+=1
                        hi-=1
                    break
        ans = 0
        for i in range(len(num)):
            ii = i
            while orig[i]!=num[i]:
                ans +=1
                ii +=1
                num[i],num[ii] = num[ii],num[i]
        return  ans


num = "5489355142"
# num = "11112"
k = 4
obj = Solution().getMinSwaps_leetcode_v2(num,k)