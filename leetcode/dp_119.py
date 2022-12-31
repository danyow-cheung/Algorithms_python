class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        output = []
        for i in range(rowIndex+1):
            if i == 0:
                prev = [1]
                output.append(prev)
            else:
                cur = [1]
                j = 1
                while j < i:
                    cur.append(prev[j - 1] + prev[j])
                    j += 1
                cur.append(1)
                output.append(cur)
                prev = cur
        return output[-1]
        # print(output)
rowIndex = 3
obj  = Solution().getRow(rowIndex)