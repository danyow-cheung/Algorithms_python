class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        hash = {}
        for i in list1:
            hash[i] = 1

        for i in list2:
            if i in hash:
                hash[i] -= 1
        ans = []

        for key,value in hash.items():
            if value==0:
                ans.append(key)

        curr ={}
        for i in ans:
            cur = list1.index(i)+list2.index(i)
            curr[i] = cur
            print(i,cur)

        print(curr)
        # print([key for key in curr.keys() if curr[key] = min(curr.keys())])
        print(min(curr.values()))
        final = []
        for key,value in curr.items():
            if value == min(curr.values()):
                final.append(key)
        print(final)
        return  final

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["KFC","Shogun","Burger King"]

# list1 = ["happy","sad","good"]
# list2 = ["sad","happy","good"]
obj = Solution().findRestaurant(list1,list2)