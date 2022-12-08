class Solution(object):

    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        if initialExperience > sum(experience) and initialEnergy > sum(energy):
            return 0

        count = 0

        for i,j in zip(energy,experience):
            if initialEnergy<= i:
                # 一次只能加一个
                initialEnergy =i+1
                count += i-initialEnergy+1

            if initialExperience<= j:
                initialExperience = j+1
                count += j-initialExperience+1

            initialEnergy = initialEnergy - i
            initialExperience = initialExperience +j

        print(count)
        return count

    def minNumberOfHours_leetcode(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        ans = 0
        for x, y in zip(energy, experience):
            if initialEnergy <= x:
                ans += x + 1 - initialEnergy
                initialEnergy = x + 1
            if initialExperience <= y:
                ans += y + 1 - initialExperience
                initialExperience = y + 1
            initialEnergy -= x
            initialExperience += y
        return ans


# 初始精力
initialEnergy = 5
# 初始经验
initialExperience = 3
# 对手精力
energy = [1,4,3,2]
# energy = [1,4]
# 对手经验
experience = [2,6,3,1]
# experience = [2,5]
#
initialEnergy = 1
initialExperience = 1
energy = [1,1,1,1]
experience = [1,1,1,50]

obj = Solution().minNumberOfHours(initialEnergy,initialExperience,energy,experience)