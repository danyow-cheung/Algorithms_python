import  statistics

class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """

        arr.sort()
        length = len(arr[1:len(arr) - 1])
        summary = sum(arr[1:len(arr) - 1])
        print(length,summary)
        print(summary//length)
        return summary // length

    def trimMean_leetcode(self,arr):
        '''python3情況下通過測試'''
        arr.sort()
        remove = int(len(arr)*0.05)
        print(remove)
        print(arr[remove:-remove])
        '''。mean
        ()函數可用於計算給定數字列表的均值/平均值。
        它返回作為參數傳遞的數據集的平均值。
        算術平均值是數據總和除以數據點數。
        它是衡量數據在範圍內變化的一組值中的中心位置的量度。
        在 Python 中，我們通常通過將給定數字的總和除以當前數字的計數來做到這一點
'''
        print(statistics.mean(arr[remove:-remove]))
        return  statistics.mean(arr[remove:-remove])

arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
# arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
# arr = [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8,2, 3, 4]

obj = Solution().trimMean_leetcode(arr)