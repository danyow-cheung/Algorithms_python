class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        salary.pop()
        salary.remove(salary[0])
        print(salary)
        
        return sum(salary)/len(salary)

salary = [4000,3000,1000,2000]
obj = Solution().average(salary)