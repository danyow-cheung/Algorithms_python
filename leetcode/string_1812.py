class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        都是奇数是黑色，都是偶数是黑色
        """
        ans = [0,0]


        map = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

        ans[0] = map[coordinates[0]]
        ans[1] = int(coordinates[1])
        if ans[0]%2==0 and ans[1]%2==0:
            return False
        elif (ans[0]+1)%2==0 and (ans[1]+1)%2==0:
            return False
        return True
        print(ans)

coordinates = "a1"
coordinates = "c7"

obj = Solution().squareIsWhite(coordinates)