UF = {}
def find(x):
    '''基本Union-find template'''
    # UF 是一個哈希映射，您可以在其中找到一組元素的根，給出一個元素。
    # UF中的key是一個元素，UF[x]是x的父元素。
    # 如果 UF[x] == x 表示 x 是其組的根。

    # 給定一個元素，找到group的root值
    if x not in UF:
        UF[x] = x
    # if x ==UF[x] 意味x是group的root
    # if x!=UF[x]  在x的父母UF[x]再次使用find函數
    # 直到我們找到根並將其設置為 UF 中 x 的父（值）。
    if x!= UF[x]:
        UF[x] = find(UF[x])
    return  UF[x]

    # 給定兩個元素 x 和 y，我們知道 x 和 y 應該在同一組中，
    # 這意味著包含 x 的組和包含 y 的組
    # 如果它們當前是單獨的組，則應合併在一起。
    # 所以我們首先使用 find 函數找到 x 的根和 y 的根。
    # 然後我們將y的根（rootY）設置為x的根（rootX）的根。
def union(x,y):
    rootX = find(x)
    rootY = find(y)

    # 將y的根（root Y）設置為x的根（root X）的根
    UF[rootX] = rootY

class Solution(object):


    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        聯合發現
        https://leetcode.com/problems/lexicographically-smallest-equivalent-string/solutions/3047517/python3-union-find-template-explanations/

        """

        UF = {}
        def find(x):
            UF.setdefault(x,x)
            if x!=UF[x]:
                UF[x] = find(UF[x])
            return  UF[x]

        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX>rootY:
                UF[rootX]=rootY
            else:
                UF[rootY] = rootX

        # union the two equivalent characters
        # at the same position from s1 and s2 into the same group
        for i in range(len(s1)):
            union(s1[i],s2[i])
        # Simply find the root of the group a character belongs to
        # note that if c is not in any group
        # we have UF.setdefault(x,x) in def find(x) to take care of it
        res = []
        for c in baseStr:
            res.append(find(c))
        return "".join(res)


s1 = "parker"
s2 = "morris"
baseStr = "parser"
obj = Solution().smallestEquivalentString(s1,s2,baseStr)