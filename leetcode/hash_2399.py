class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        d= {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i]
            else:
                d[s[i]].append(i)
        print(d)
        d = dict(sorted(d.items(),key =lambda x:x[0]))

        print(d)
        for i in d:
            diff = d[i][1] -d[i][0]-1
            index = ord(i)-97
            if distance[index]!=diff:
                return False
        return  True


s = "abaccb"
distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
obj = Solution().checkDistances(s,distance)