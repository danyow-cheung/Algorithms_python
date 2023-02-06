class Solution(object):
    def longestPalindrome_hashmap(self,words):
        '''https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/solutions/2715749/longest-palindrome-by-concatenating-two-letter-words/
        '''
        import collections
        count = collections.Counter(words)
        ans = 0 
        central = False 
        print(count)

        for word,count_of_the_word in count.items():
            # if the word is a palindrome
            if word[0]==word[1]:
                if count_of_the_word%2==0:
                    ans += count_of_the_word
                else:
                    ans += count_of_the_word -1 
                    central =True
            # 考慮不是回文字符串的元素
            elif word[0]<word[1]:
                ans += 2 * min(count_of_the_word, count[word[1] + word[0]])
        if central:
            ans +=1 
        return 2*ans

    def longestPalindrome_twoDimension(self):
        '''https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/solutions/2715749/longest-palindrome-by-concatenating-two-letter-words/
        '''
        alpha_size =26 
        count = [[0] for j in range(alpha_size) for i in range(alpha_size)]
        for word in words:
            count[ord(word[0]) - ord('a')][ord(word[1]) - ord('a')] += 1 
        ans = 0 
        central = False
        for i in range(alpha_size):
            if count[i][j]%2==0:
                ans += count[i][i]
            else:
                ans += count[i][i] -1 
                central = True
            for j in range(i+1,alpha_size):
                ans += 2*min(count[i][j],count[j][i])
        if central:
            ans +=1 
        return 2*ans




    def one_list_length(self,lst):
    
        res = "".join(lst)
        print(type([res]),res[::-1],res)

        if res==res[::-1]:
            # print(res)

            return True

        return False 

    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        太多規則需要去滿足，代碼越寫越多--nein
        """
        m = len(words)  
        if m==1:
            # 是回文字符串返回2
            if self.one_list_length(words):
                return 2 
            else:
                # 否則返回0
                return 0 

        # import collections
        # 每個元素的長度都是2，回文字串只要滿足每個都是偶數的平方就可以
        res = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i]==words[j][::-1]:
                    res.append(words[i])
                    res.append(words[j])

        print(res)
        ans = sum(len(i) for i in res)

        if m%2==0:
            print(ans)

            return ans
        elif res==[]:
            # 去每個元素裡面查找有沒有回文字符串
            for i in words:
                if self.one_list_length(i):
                    return 2 
                else:
                    # 否則返回0
                    return 0 

        else:
            # 先找到這個元素
            left= [i for i in words if i not in res ]
            print("left",left)

            # 判斷這個字符是不是回文
            if left==left[::-1]:
                print(ans+2)

                return ans+2
words = ["lc","cl","gg"]
words = ["ab","ty","yt","lc","cl","ab"]
# words = ["cc","ll","xx"]

words = ['aa']
words = ['bd']
words = ["tw","az","fb"]

# obj = Solution().longestPalindrome(words)
obj = Solution().longestPalindrome_hashmap(words)