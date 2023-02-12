import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        https://leetcode.com/problems/minimum-window-substring/solutions/164122/minimum-window-substring/
        """
        if not s or not t:
            return ""
        # dictionary which keeps a count of all the unique characters in t 
        dict_t = collections.Counter(t)
        # number of unique characteres in t,which need to be present in the desired window
        required = len(dict_t)

        # left and right pointer 
        l = 0 
        r = 0

        # formed is used to keep track of how many unique characters in t are present in the 
        # current window in its desired frequency
        formed = 0
        # dictionary which keeps a count of all the unique characters in the current window
        window_counts = {}
        # ans tuple of the form ( window length,left,right)
        ans = float('inf'),None,None
        while r<len(s):
            # add one character from the right to the window 
            character = s[r]
            window_counts[character] = window_counts.get(character,0)+1 

            # if the frequency of the current character added equals to the des
            if character in dict_t and window_counts[character]==dict_t[character]:
                formed +=1 
            while l<=r and formed==required:
                character = s[l]

                if r-l+1<ans[0]:
                    ans = (r-l+1,l,r)
                
                window_counts[character]-=1 
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -=1 
                l+=1 
            r+=1 
        return ""if ans[0]==float('inf')else s[ans[1]:ans[2]+1]
        
    

s = "ADOBECODEBANC"        
t = "ABC"
obj = Solution().minWindow(s,t)