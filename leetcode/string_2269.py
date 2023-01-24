class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        ans = []
        string = str(num)
        for i in range(len(string)):
            for j in range(i+1,len(string)):
                print(string[i:j+1])
                if len(string[i:j+1])==k:
                    ans.append(string[i:j+1])
        print(ans)
        count = 0

        for i in ans:
            if  int(i)!=0 and num%int(i) ==0:
                count +=1 
        print(count)
        return count
    def divisorSubstrings_leetcode(self,num,k):
        i = 0
        count = 0
        number = str(num)
        while i < len(number):
            if i + k <= len(number):
                s = number[i: i + k]
                if int(s) != 0 and num % int(s) == 0:
                    count += 1
                i += 1
            else:
                break
        return count


num = 240
k = 2

num = 430043
k = 2

num = 2 
k =1
obj = Solution().divisorSubstrings(num,k)