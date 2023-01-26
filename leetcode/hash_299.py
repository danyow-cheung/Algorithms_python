import collections
class Solution(object):
    def calculate_a(self,secret,guess):
        count_a = 0
        map_ = {}
        for i , j in zip(secret,guess):
            # print(i,j)
            if i==j:
                count_a +=1 
            else:
                if i not in map_:
                    map_[i] =1 
                elif i in map_:
                    map_[i]+=1
                if j not in map_:
                    map_[j] =1 
                elif i in map_:
                    map_[j]+=1
                
        print(map_)
        count_b = 0 
        for val,cnt in map_.items():
            if cnt>=2:
                count_b+=1
        # count_b = count_b*(count_b)
        print(str(count_a)+'A'+str(count_b)+"B")

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # map_={}
        # for i,j in enumerate(secret):
        #     map_[j] = 1 
        # print(map_)
        # count_a = 0
        # count_b = 0
        
        # for i,j in enumerate(guess):
        #     # 當前index在hash中
        #     if map_[j]:
        #         map_[j] -=1 
        #     else:
        #         map_[j] =1 

        # print(map_)
        
        # res = ['0','A','0','B']

    def getHint_leetcode(self, secret, guess):
        count = collections.Counter(secret)
        x,y = 0,0 
        for i in range(len(guess)):
            if guess[i]==secret[i]:
                x+=1 
                count[secret[i]]-=1
        
        for i in range(len(guess)):
            if guess[i] in count and secret[i]!=guess[i] and count[guess[i]]>0:
                y+=1 
                count[guess[i]]-=1
        return str(x)+"A"+str(y)+"B"
        

secret = "1807"
guess = "7810"

secret = "1123"
guess = "0111"
secret = "1122"
guess = "2211"

obj = Solution().calculate_a(secret,guess)