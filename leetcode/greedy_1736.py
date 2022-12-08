class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hour = time[0:2]
        minute = time[3:5]

        cur = ""
        print('hour=',hour)
        for i in hour:
            cur+=i

            if i == '?':
                print('cur',cur)



time = "2?:?0"
obj =Solution().maximumTime(time)