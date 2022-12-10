class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        dict_ = {}

        for i in range(len(sentence)):
            if sentence[i] not in dict_:
                dict_[sentence[i]] = 1
            elif sentence[i] in dict_.keys():
                dict_[sentence[i]] +=1
        print(dict_)
        print(len(dict_.keys()))
sentence = "thequickbrownfoxjumpsoverthelazydog"
# sentence = 'leetcode'
obj = Solution().checkIfPangram(sentence)