class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        print(command.replace("()","o").replace("(al)",'al'))

command = "G()(al)"
obj = Solution().interpret(command)