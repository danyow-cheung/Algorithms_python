import collections


class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        res =[]
        for i in words:
            print(i)
            cur_lst = []
            for j in range(len(i)):
                if j+1<len(i):
                   cur = -ord(i[j]) +ord(i[j+1])
                   cur_lst.append(int(cur))
            res.append(cur_lst)

        print(res)

        for i in range(len(res)):
            if res.count(res[i])==1:
                return words[i]



# print('cur',i[j],ord(i[j]),ord(i[j+1]))

words = ["adc","wzy","abc"]
words= ["ddd","poo","baa","onn"]
obj =Solution().oddString(words)