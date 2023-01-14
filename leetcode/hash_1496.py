class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        hash_ = {"x":0,"y":0}
        print(hash_)
        for i in path:
            # print(i)
            if i =='N':
                hash_["y"] += 1
            elif i=='S':
                hash_["y"] -= 1

            elif i=='E':
                hash_['x'] +=1
            else:
                hash_['x'] -=1
            # print(i,sum(hash_.values()))
            if hash_["x"]==hash_['y']==0:
                return True

        return  False

    def isPathCrossing_leetcode(self, path):
        coor = [0,0]
        coors =[[0,0]]
        for i in path:
            print(coor,coors)
            if i=="N":coor[1]+=1
            elif i=='S':coor[1]-=1
            elif i=='E':coor[0]+=1
            else:coor[0]-=1

            if coor in coors:
                return True
            coors.append(coor[:])
        return False


path = "NES"
# path = "NESWW"
path = "ES"
obj = Solution().isPathCrossing_leetcode(path)