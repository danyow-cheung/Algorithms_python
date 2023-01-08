class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        s = "0"*len(target)
        if s==target:
            return 0

        print(s)
        target_lst = list(target)

        idx = []
        left = 0
        while left<len(target)-1:
            if target_lst[left]==target_lst[left+1]=="1":
                # print(target_lst[left],left)
                idx.append([left,left+1])
            elif target_lst[left]=="1":
                # 儲存下標
                idx.append(left)
            else:
                #是0的情況，直接跳
                pass

            left+=1

    def minFlips_leetcode(self, target):
        flips = 0
        status = '0'
        for c in target:

            if c!=status:
                flips+=1
                # 紀錄上一元素的狀態
                status='0' if status=='1' else '1'
        print(flips)


target = '10111'
# target = "101"

obj = Solution().minFlips_leetcode(target)