import collections


class Solution(object):
    '''檢查字典裡面有沒有零數'''
    def check(self,hash_):
        for value in hash_.values():
            if value>0:
                return False
        return True
    '''在數組中找到最短的元素'''
    def find_shortest(self,arr):
        length  = float('INF')
        for i in arr:
            length = min(length,len(i))
        for i in arr:
            if len(i) == length:
                return i


    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        ans = []
        licensePlate = licensePlate.lower().replace(" ",'')
        license = []
        for i in licensePlate:
            if i.isalpha():
                license.append(i)
        count = collections.Counter(license)
        print('count = ',count)
        for i in words:
            cur_len = count.copy()
            for w in i:
                if w in cur_len:
                    cur_len[w]-=1

            if self.check(cur_len):
                ans.append(i)
            print(cur_len)

        ans = self.find_shortest(ans)
        print(ans)
        return ans
licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]

licensePlate = "1s3 456"
words = ["looks","pest","stew","show"]

obj = Solution().shortestCompletingWord(licensePlate,words)