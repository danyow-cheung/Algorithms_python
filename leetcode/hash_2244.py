class Solution(object):
    def countTimes(self,value):
        count = 0
        while value>0:
            # print('value',value)
            if value>=3:
                value -=3
            else:
                value -= 2
            count+=1

        print("countTimes",count)
        return  count

    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        ans = 0
        tasks.sort()
        hash_  ={}

        for i in tasks:
            if i not in hash_:
                hash_[i] = 1
            else:
                hash_[i]+=1
        print(hash_)
        for key,value in hash_.items():
            if value ==1:
                return -1
            else:
                print('次数超过最大3次的')
                print(key,value,type(value))
                ans += self.countTimes(value)

        print('ans=',ans)
        if ans:
            return  ans
        else:
            return  -1

tasks = [2,2,3,3,2,4,4,4,4,4]
tasks = [7,7,7,7,7,7]
obj = Solution().minimumRounds(tasks)