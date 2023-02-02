class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        重新排序之後出現arr[2*i+1]==2*arr[2*i]

        """
        # arr.sort()
        # for i in range(len(arr)//2-1):
        #     print(arr[i])
        #     if arr[2*i+1]==2*arr[2*i]:
        #         print('ture')
        #         return True
        # return False
        '''
        Let's check elements in order of absolute value.
         When we check an element x and it isn't used, 
         it must pair with 2*x. 
         
         We will attempt to write x, 2x - 
         if we can't, then the answer is false. 
         If we write everything, the answer is true.
        '''
        import collections
        count = collections.Counter(arr)
        # 以絕對值的形式進行排序
        for x in sorted(arr,key=abs):
            # print(x,count[x])
            if count[x]==0:continue
            if count[2*x]==0:return False
            count[x]-=1 
            count[2*x]-=1 
        return True

arr = [3,1,3,6]
arr = [-4,-2,2,4]

obj = Solution().canReorderDoubled(arr)
