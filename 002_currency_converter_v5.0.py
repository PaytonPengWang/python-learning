"""
CNY/汇率 = USD

## 思考
能否保存多个货币的汇率，而不是单一的汇率  Python中的集合操作 案例5
能否实时获取汇率？   Python爬虫实现  案例8
"""





# 主函数
def main():
    RATE = 6.77
    EXIT = 'Q'

    unconvert_currency_str = input('请输入带单位的货币金额(退出Q)：')

    while unconvert_currency_str != EXIT:
        

        currency = unconvert_currency_str[-3:]
        amount_str = unconvert_currency_str[:-3]
        

        if currency == 'USD':
            result  = "CNY" + str(convert_currency(amount_str,RATE))
        elif currency == "CNY":
            result = "USD" + str(convert_currency(amount_str,1/RATE))
        else:
            result = "unvalid currency"



        print(result)

        unconvert_currency_str = input('请输入带单位的货币金额(退出Q)：')
    else:
        print("程序退出")

convert_currency = lambda amount_str,rate: eval(amount_str) * rate

if __name__ == '__main__':
    main()
    


