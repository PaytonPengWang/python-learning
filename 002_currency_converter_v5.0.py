"""
CNY/汇率 = USD
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
    


