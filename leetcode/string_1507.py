class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        month ={1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun",
                7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct",11:"Nov", 12:"Dec"}
        data = date.split()
        print(data)
        year = data[-1]
        print(year,type(year))
        from datetime import  datetime
        date_obj = datetime.strptime(date,"%y/%d/%m")
        print(date_obj,type(date_obj))

        # for i in date:
            # print(i)
date = '20th Oct 2052'
# 2052-10-20"
obj = Solution().reformatDate(date)