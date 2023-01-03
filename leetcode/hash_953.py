class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        實現步驟
        - 初始化一個 hashmap/array 來記錄每個字母和它在order.
        - 遍歷words並比較每對相鄰的單詞。
            1. 遍歷每個字母以找到 和 之間的第一個不同words[i]字母words[i + 1]。
            2. 如果words[i + 1]在之前結束words[i]並且沒有找到不同的字母，那麼我們需要返回 false 因為words[i + 1]應該在之前words[i]（例如，apple和app）。
            3. 如果我們找到第一個不同的字母並且兩個單詞的順序正確，那麼我們可以退出當前迭代並繼續處理下一對單詞。
            4. 如果我們發現第一個不同的字母並且兩個單詞的順序錯誤，那麼我們可以安全地返回 false。
        - 如果我們到達這一點，則意味著我們已經檢查了所有相鄰單詞對並且它們都已排序。因此我們可以返回 true。

        """
        order_map = {}
        for index,val in enumerate(order):
            # print(index,val)
            order_map[val] = index

        for i in range(len(words)-1):
            for j in range(len(words[i])):
                # print(words[i],words[i][j])
                # if we do not find a mismatch letter between words[i] and words[i+1]
                # we need to examine the case when words are like ("apple","app")
                if j>= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if order_map[words[i][j]]>order_map[words[i+1][j]]:
                        return False
                    break
        return True
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
obj  = Solution().isAlienSorted(words,order)