class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        ans_color  = []
        ans_rods = []
        dict_ ={}
        for i in range(0,len(rings),2):
            print(rings[i])

            # # 字母
            # if i.isalpha():
            #     ans_color.append(i)
            # # 数字
            # if i.isdigit():
            #     ans_rods.append(i)

        # print(ans_rods)
        # print(ans_color)
        # for i in range(len(ans_rods)):
        #
        #     dict_[ans_rods[i]] = ans_color[i]
        # print(dict_)

rings = "B0B6G0R6R0R6G9"
obj = Solution().countPoints(rings)