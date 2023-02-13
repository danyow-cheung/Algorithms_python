import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        """
       
        # count= collections.Counter(strs)
        # print(count)
        res = {}
        for i in strs:
            # count= (i for i in collections.Counter(i).keys())
            # print(count,)
            count = []
            for i in collections.Counter(i).keys():
                # count.index()
                count.append(i)
            print(count)
            count = tuple(count)

            if count not in res:
                res[count]=1 
            else:
                res[count]+=1 
        print(res)

    def groupAnagrams_leetcode(self,strs):
        '''https://leetcode.com/problems/group-anagrams/solutions/127405/group-anagrams/'''
        # categorize by sorted string 
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        print(ans)
        return ans.values()
    
    def groupAnagrams_leetcode_2(self,strs):
        '''https://leetcode.com/problems/group-anagrams/solutions/127405/group-anagrams/'''
        # categorize by sorted string 
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0]*26 
            for c in s:
                count[ord(c)-ord('a')]+=1 

            ans[tuple(count)].append(s)
        print(ans)
        return ans.values()
    

strs = ["eat","tea","tan","ate","nat","bat"]
# obj = Solution().groupAnagrams(strs)
obj = Solution().groupAnagrams_leetcode(strs)
