"""
CNY/汇率 = USD
"""

RATE = 6.77
EXIT = 'Q'

unconvert_currency_str = input('请输入带单位的货币金额(退出Q)：')

while unconvert_currency_str != EXIT:
    

    currency = unconvert_currency_str[-3:]
    amount_str = unconvert_currency_str[:-3]
    amount = eval(amount_str)

    if currency == 'USD':
        result  = "CNY" + str(amount*RATE)
    elif currency == "CNY":
        result = "USD" + str(amount/RATE)
    else:
        result = "unvalid currency"



    print(result)

    unconvert_currency_str = input('请输入带单位的货币金额(退出Q)：')
else:
    print("程序退出")

