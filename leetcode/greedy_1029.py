class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        print(n)
        a = 0
        b = 0
        res =0
        # costs.sort()
        print(costs)
        # exit(0)
        for i in costs:
            if abs(a-b)<1:
                res += min(i)
                if res ==i[0]:
                    a+=1
                else:
                    b+=1
            else:
                if a<=b:
                    res += i[0]
                    a+=1
                else:
                    res += i[1]
                    b+=1

        print(a,b)
        print(res)

    def twoCitySchedCost_leetcode(self,costs):
        FirstCity = [i for i,j in costs]
        Diff = [j-i for i,j in costs]
        print(FirstCity,Diff)
        return sum(FirstCity)+sum(sorted(Diff)[:len(costs)//2])
costs = [[10,20],[30,200],[400,50],[30,20]]
# costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
obj = Solution().twoCitySchedCost_leetcode(costs)