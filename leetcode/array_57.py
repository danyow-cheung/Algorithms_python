class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        太複雜了看解析
        """
        min_val = newInterval[0]
        max_val = newInterval[1]
        print("original",intervals)
        res = []
        # 輸入為空的情況
        if len(intervals)==0:
            return  [newInterval]

        # elif max_val>intervals[-1][1]:
        #     return
        for i ,j in intervals:
            # print(i,j)
            # 找起點
            if min_val >j:
                res.append([i,j])
            elif min_val>i:
                # min_val已經在縮小到這個區間
                # 判斷max_val的數值
                if max_val<j:
                    # 情況1：也被包含，不做任何操作
                    res.append([i,j])

                elif max_val>j:
                     #情況2：擴大到最大的數組那位
                    res.append([i,max_val])
                    # if max_val
            if max_val<i:
                res.append([i,j])
            # elif
            elif max_val==i:
                res.append([max_val,j])
            elif max_val>j and min_val<=i:
                res.append([min_val,max_val])


        print("res",res)
        # n = len(res)-1
        # ans = res.copy() #->
        ans = res[:]
        for i in range(len(res)-1):
            print("view",ans,res[i][1])
            if res[i][1]==res[i+1][0]:

                ans[i][0],ans[i][1] = res[i][0],res[i+1][1]
                del ans[i+1]
                print('show',ans[i],ans[i+1])
                # ans.append([res[i][0],res[i+1][1]])
        print("res",res,"ans",ans)
        return ans

    def insert_leetcode(self, intervals, newInterval):
        N = len(intervals)
        i = 0
        res = []
        # add non-overlapping intervals before new_interval to res
        while i<N and intervals[i][1]<newInterval[0]:
            res.append(intervals[i])
            i+=1
        print(res)
        res.append(newInterval)
        # merge overlapping intervals with new_interval
        while i<N and min(res[-1][1],intervals[i][1])>=max(intervals[i][0],res[-1][0]):
            res[-1] = min(res[-1][0],intervals[i][0]),max(res[-1][1],intervals[i][1])
            i+=1
        # add the rest of the non-overlapping intervals to res
        while i<N:
            res.append(intervals[i])
            i+=1
        return res



intervals = [[1,3],[6,9]]
newInterval = [2,5]
#
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]


intervals = [[1,5]]
newInterval = [1,7]
obj = Solution().insert_leetcode(intervals,newInterval)