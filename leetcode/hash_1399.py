class Solution(object):
    def int2str(self,numbers):
        ans =0
        num = str(numbers)
        for i in num:
            ans+=int(i)
        return  ans

    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        给你一个整数 n。请你先求出从 1到 n 的每个整数 10 进制表示下的数位和（每一位上的数字相加），
        然后把数位和相等的数字放到同一个组中。
        请你统计每个组中的数字数目，并返回数字数目并列最多的组有多少个。

        """
        hash = {}

        for i in range(1,n+1):
            sum_val = self.int2str(i)
            if sum_val not in hash:
                hash[sum_val]=1
            else:
                hash[sum_val]+=1
        print(hash)
        max_val = max(hash.values())
        print(max_val)
        count= 0
        for key,value in hash.items():
            if value == max_val:
                count +=1


        return count



n =13
# n =2
obj = Solution().countLargestGroup(n)