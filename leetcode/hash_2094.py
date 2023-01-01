class Solution(object):
    def contain(self,num,digits):

        number = str(num)
        hash_ = {}
        for i in number:
            if int(i) in digits:
                hash_[i] = 1
            if len(hash_)==3:
                break
        print(hash_)
        if sum(hash_.values())==3:
            return True
        return False

    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res =set()

        for i in range(100,999):
            if i%2==0 and self.contain(i,digits):
                    res.add(i)

        print(res)
        ans = []
        for i in res:
            print(i)
            ans.append(i)

        # ans = [i for i  in res ]
        print(sorted(ans))
        print( sorted([i for i in res]))


digits = [2,1,3,0]
digits = [2,2,8,8,2]

# obj = Solution().findEvenNumbers(digits)
obj = Solution().contain(222,digits)