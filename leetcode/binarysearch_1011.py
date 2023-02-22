class Solution(object):
    def check(self,weights,c,days):
        '''检查c容量货物能否在days内运送完'''
        dayNeeded = 1 
        currentLoad = 0 
        for weight in weights:
            currentLoad += weight
            if currentLoad>c:
                dayNeeded+=1 
                currentLoad = weight
        return dayNeeded<= days


    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        看的官方指导，本人没那么厉害
        """
        totalLoad = 0 
        maxLoad = 0 
        for weight in weights:
            totalLoad += weight
            maxLoad = max(maxLoad,weight)
        l = maxLoad
        r = totalLoad

        while l<r:
            mid = (l+r)/2 
            if self.check(weights,mid,days):
                r = mid 
            else:
                l = mid+1 
        return l  





weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
obj = Solution().shipWithinDays(weights,days)