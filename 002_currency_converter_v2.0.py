"""
CNY/汇率 = USD
"""

RATE = 6.77

unconvert_currency_str = input('请输入带单位的货币金额：')

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

# cnyAmountFlt = eval(cnyAmountStr)


# usdAmount = cnyAmountFlt / RATE

# print('美元(USD)金额是：',usdAmount)
