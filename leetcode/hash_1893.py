class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """

        # for i in ranges:
            # print(i)
        x = []
        for i in range(left,right+1):
            x.append(i)
        print(x)
        count =0
        for i in x:
            for j in ranges:
                if i in range(j[0], j[1] + 1):
                # if i in j:
                    print(i,j)
                    count +=1
        if count==len(x):
            return True
        return False

    def isConvered_leetcode(self,ranges,left,right):

        res = [0] * 51
        for start, end in ranges:
            for i in range(start, end + 1):
                res[i] = 1
        return all(res[left:right + 1])

ranges = [[1,2],[3,4],[5,6]]
left = 2
right = 5
obj = Solution().isCovered(ranges,left,right)