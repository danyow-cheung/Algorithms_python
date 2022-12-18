class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ans = set()
        for i in emails:
            plus_idx = 0
            sym_idx = 0
            cur = i

            print('original = ',cur)
            for j in range(len(i)):
                if i[j] == '.':
                    j += 1
                elif i[j] == '+' and plus_idx == 0:
                    plus_idx = j
                    # break
                elif i[j] == '@':
                    sym_idx = j
            # print(i[0:plus_idx],i[sym_idx:])
            if plus_idx != 0:
                cur = i[0:plus_idx].replace(".", "") + i[sym_idx:]
            elif plus_idx==0:
                cur = i[0:sym_idx].replace('.','')+i[sym_idx:]
            ans.add(cur)
            print('after=',cur)

        return len(ans)


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
emails=["test.email+alex@leetcode.com", "test.email@leetcode.com"]
obj = Solution().numUniqueEmails(emails)