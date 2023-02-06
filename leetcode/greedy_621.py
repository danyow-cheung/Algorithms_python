import collections
class Solution(object):
    def leastInterval_leetcode(self, tasks, n):
        freq = collections.Counter(tasks)
        max_freq = max(freq.values())
        freq = list(freq.values())

        max_freq_ele_count = 0 
        i = 0
        while i<len(freq):
            if freq[i]==max_freq:
                max_freq_ele_count+=1 
            i+=1 
        ans = (max_freq-1)*(n+1)+max_freq_ele_count
        return max(ans,len(tasks))
        
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n==0:
            return len(tasks)
        
        count = collections.Counter(tasks)
        print(count)

        # 構建任務的列表
        res = []
        # res.append()
        for key,val in count.items():
            res.append(key)
            val -=1 
        print(res)





tasks = ["A","A","A","B","B","B"]
n = 2

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2

obj = Solution().leastInterval(tasks,n)
