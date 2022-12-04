class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        # 相差的小时数字
        current_time = []
        correct_time = []
        ans = 0
        for i in current:
            if i!=':':
                current_time.append(int(i))
        for i in correct:
            if i != ':':
                correct_time.append(int(i))
        hour_diff = abs((current_time[0]-correct_time[0]))*10+abs(correct_time[1]-current_time[1])
        minu_diff = abs((current_time[2]-correct_time[2]))*10+abs(correct_time[3]-current_time[3])

        print(current_time, correct_time)

        diff = hour_diff*60 + minu_diff

        while diff>0:
            if diff-60>=0:
                diff-=60
            elif diff-15>=0:
                diff-=15
            elif diff-5>=0:
                diff-=5
            else:
                diff-=1
            ans+=1


        print(ans)
        return ans


current = "02:30"
correct = "04:35"

current = "12:24"
correct = "12:50"


obj = Solution().convertTime(current,correct)