"""
    作者：王鹏
    功能：52周存钱挑战
    日期：1/1/2019
    v2.0 新增：记录每周的存款数
"""
import math


def main():
    INCREASE_MONEY = 10
    TOTAL_WEEK = 52

    # 每周存入的金额
    money_per_week = INCREASE_MONEY
    # 第几周
    week = 1
    account_list = []
    
    while week <= TOTAL_WEEK:
        account_list.append(money_per_week)

        print("第{0}周，存入{1}元，账户累计：{2}".format(week,money_per_week,math.fsum(account_list)))
        week += 1
        
        money_per_week += INCREASE_MONEY



if __name__ == "__main__":
    main()