class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        奇數遞減，偶數遞增
        """
        odd = []
        even = []
        for i in nums:
            if i%2==1:
                odd.append(i)
            else:
                even.append(i)
        # print('orginal',nums)
        # print(odd,even)
        odd.sort(reverse=True)
        even.sort()
        # print(odd, even)

        x = 0
        y = 0
        for i in range(len(nums)):
            # print(i&1)
            if nums[i]%1==0:
                # print(nums[i])
                nums[i] = odd[x]
                x+=1
            else:
                nums[i] = even[y]
                y+=1
        print(nums)
        #[9,46,15,45,15,41,27,34,32,31,33,31,36,26,36,16,44,6]

        return  nums
    def sortEvenOdd_leetcode(self,nums):
        even = []
        odd = []
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort(reverse=True)
        even.sort()
        i,j=0,0
        for i in range(len(nums)):
            if i&1:
                nums[i] = odd[i]
                j+=1
            else:
                nums[i] = even[j]
                j+=1
        return  nums

nums = [4,1,2,3]
nums =[36,45,32,31,15,41,9,46,36,6,15,16,33,26,27,31,44,34]
obj = Solution().sortEvenOdd(nums)