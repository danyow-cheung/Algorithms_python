import collections


class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        brute force -- TLE
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        ans = []
        for  i in range(len(aliceSizes)):
            for j in range(len(bobSizes)):
                # print('alice,bob', aliceSizes[i], bobSizes[j])
                alice_sum = aliceSizes[0:i]+aliceSizes[i+1:]
                bob_sum = bobSizes[0:j]+bobSizes[j+1:]
                # print('alice sum ,bob sum ',alice_sum,bob_sum)
                if len(ans)==2:
                    break
                    # return  ans
                if sum(alice_sum)+bobSizes[j]==sum(bob_sum)+aliceSizes[i]:
                    ans.append(aliceSizes[i])
                    ans.append(bobSizes[j])


        print(ans)
        return ans


    def fairCandySwap_hash(self,aliceSizes,bobSizes):
        Sa,Sb = sum(aliceSizes),sum(bobSizes)
        setB = set(bobSizes)
        for i in aliceSizes:
            if i+(Sb-Sa)/2 in setB:
                return [i,i+(Sb-Sa)/2]



# aliceSizes = [1,1]
# bobSizes = [2,2]s

aliceSizes = [1,2,5]
bobSizes = [2,4]
obj = Solution().fairCandySwap_hash(aliceSizes,bobSizes)