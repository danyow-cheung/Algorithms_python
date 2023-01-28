
import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones)!=1:
            
            stones.sort()
            print(stones)
            fir_val =stones[-1]
            sec_val =stones[-2]
            if fir_val==sec_val:
                del stones[-1],stones[-2]
            else:
                
                del stones[-1],stones[-2]
                diff = fir_val-sec_val
                stones.append(diff)
        print('after while',stones)   
        return 0 
    
    def lastStoneWeight_leetcode(self, stones):
        # https://leetcode.com/problems/last-stone-weight/solutions/1921241/python-beginner-friendly-optimisation-process-with-explanation/
        # sort and insert
        stones.sort()
        while stones:
            # 最重的stones
            s1 = stones.pop()
            if not stones:
                return s1 
            s2 = stones.pop()
            if s1>s2:
                # 留下来的stone会是 s1-s2
                # loop through stones to find the index to insert the stone 
                for i in range(len(stones)+1):
                    if i==len(stones) or stones[i]>=s1-s2:
                        stones.insert(i,s1-s2)
                        break
            # elif s1==s2:
                # both stones are destroyed
                # pass 
        return 0 


    def lastStoneWeight_heapq(self, stones):
        # https://leetcode.com/problems/last-stone-weight/solutions/3027670/python-heapq-min-with-negative-values-equivalent-to-heap-max/
        s = [-s for s in stones]
        heapq.heapify(s)
        while len(s)>1:
            heapq.heappush(s,-abs(heapq.heappop(s)-heapq.heappop(s)))
        # print(s)

        return -s[0]



stones = [2,7,4,1,8,1]
obj = Solution().lastStoneWeight_heapq(stones)
