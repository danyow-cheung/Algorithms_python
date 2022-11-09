class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        是每位学生都有座位的最少移动次数
        一个房间里有 n个座位和 n名学生，房间用一个数轴表示。给你一个长度为 n 的数组 seats，其中seats[i] 是第 i个座位的位置。同时给你一个长度为 n的数组students，其中students[j]是第 j位学生的位置。

        你可以执行以下操作任意次：

        增加或者减少第i位学生的位置，每次变化量为 1（也就是将第 i 位学生从位置 x 移动到 x + 1 或者 x - 1）
        请你返回使所有学生都有座位坐的 最少移动次数，并确保没有两位学生的座位相同。

        请注意，初始时有可能有多个座位或者多位学生在 同一 位置。
        """
        # 从leetcode上学习
        for a,b in zip(sorted(students),sorted(seats)):
            print(a,b,abs(a-b))
        return sum(abs(a - b) for a, b in zip(sorted(students), sorted(seats)))


seats = [3,1,5]
students = [2,7,4]
obj = Solution().minMovesToSeat(seats,students)