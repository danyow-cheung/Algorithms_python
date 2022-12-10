class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """

        single_key = []
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        ans = ""
        for i in key:
            if i.isalpha() and i not in single_key:
                single_key.append(i)
        dict_ = {}
        for i in range(len(single_key)):
            dict_[single_key[i]] = letters[i]
        print(dict_)
        for i in message:
            print(i)
            if i.isalpha():
                i = dict_[i]
            ans+=i


        print(ans)
        return ans

key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
obj = Solution().decodeMessage(key,message)