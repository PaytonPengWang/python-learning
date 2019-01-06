"""
    作者：王鹏
    功能：判断一年中的第几天
    日期：3/1/2019
    
    输入某年某月每日，判断这一天是这一年的第几天？
    分析：
    1.每个月份的天书不同
    2.闰年和平年的2月份天数不同
    3.闰年判断
        四年一闰，百年不闰，四百年再闰

    v2.0新增： 用列表替换元组
    v3.0新增： 使用字典类型来存储
"""
from datetime import datetime

def is_leap_year(year):
    int_year = 0
    if type(year) != int:
        int_year = int(year)
    else:
        int_year = year
    
    if ((int_year % 4 == 0 and int_year % 100 != 0) or int_year % 400 == 0):
        return True
    else:
        return False

def main():
    input_str_date = input("请输入日期(yyyy/mm/dd)")
    input_date = datetime.strptime(input_str_date,"%Y/%m/%d")

    year = input_date.year
    month = input_date.month
    day = input_date.day

    month_day_dict = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }

    # 包含30天的 月份集合
    # _30_days_month_set = {4,6,9,11}
    # _31_days_month_set = {1,3,5,7,8,10,12}

    days = 0

    # for i in range(1,month):
    #     if i in _30_days_month_set:
    #         days+=30
    #     if i in _31_days_month_set:
    #         days+=31
    #     if i == 2 and is_leap_year(year):
    #         days+=29
    #     elif i==2:
    #         days+=28
    # days+=day
    # days_in_month_tup = (31,28,31,30,31,30,31,31,30,31,30,31)
    # days = sum(days_in_month_tup[:month-1]) + day

    # if is_leap_year(year) and month > 2:
    #     days += 1
    for i in range(1,month):
        days += month_day_dict[i]
    days+=day

    print(days)
            

if __name__ == "__main__":
    main()