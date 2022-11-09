class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        统计匹配检索规则的物品数量
        """
        res=0

        for i in items:
            # i[0] --type
            # i[1] --color
            # i[2] -- name

            if ruleKey == 'color':
                # print(i[1])
                if i[1]==ruleValue:
                    print(i)
                    res+=1

            elif ruleKey == 'type':
                # print(i[0])
                if i[0]==ruleValue:
                    print(i)
                    res+=1
            elif ruleKey == 'name':
                # print(i[2])
                if i[2]==ruleValue:
                    print(i)
                    res+=1
        print(res)

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
obj = Solution().countMatches(items,ruleKey,ruleValue)