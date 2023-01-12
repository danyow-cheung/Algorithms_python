class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        hash_ = {}

        left = 0
        while left<len(candidates):
            pass

    def largestCombination_leetcode(self, candidates):
        return max(sum(n & (1 << i) > 0 for n in candidates) for i in range(0, 24))
candidates = [16, 17, 71, 62, 12, 24, 14]
obj = Solution().largestCombination(candidates)