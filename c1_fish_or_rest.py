'''问题描述
「中国有句俗语叫“三天打鱼两天晒网”。
某人从1990年1月1日起便开始“三天打鱼两天晒网”
问这个人在以后的某一天中是“打鱼”还是“晒网」
'''

'''步骤
1.统计从1990年1月1日到指定日期的天数
2.三天打鱼两天晒网，统计的天数要/5
3.根据余数判断结果
123-打鱼，其余晒网
'''


'''算法实现
统计天数还要考虑到闰年的情况
「如果能被4整除并且不能被100整除或者能被400整除，则该年是闰年，否则不是闰年。」---使用%
'''

'''算法核心'''
def count_Day(day):
    #若为闰年则执行totalDay=totalDay+366，否则执行totalDay=totalDay+365；
    #根据月份再进行加
    # 定义一个数组存储每个月的天数
    perMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    totalDay = 0 
    year = 1990
    
    # 循环加
    while year<day['year']:
        res = runYear(day['year'])
        if res == 1:totalDay+366
        else:totalDay+365
        year+= 1
    
    if runYear(day['year'])==1:
        perMonth[2]+= 1
    i = 0 
    #增加今年以来的月份数

    while i < day['month']:
        totalDay += perMonth[i]
        i+= 1
    # 增加这个月的天数
    totalDay += day['day']
    return totalDay
    

# 判断是否是闰年的函数
def  runYear(year):
    if (year % 4== 0 and year%100!= 0 ) or (year % 400 ==0):
        return 1 
    else:
        return 0
    


print("please input 指定日期 包括年,月,日 如:1999 1 31")
year, month, day = [int(i) for i in input().split()]
# 定义一个字典
today = {"year":year,"month":month,"day":day}



totalDay = count_Day(today)
result = totalDay % 5 
if result>0 and result<4:
    print("打鱼")
else:
    print("晒网")

