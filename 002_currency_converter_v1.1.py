"""
CNY/汇率 = USD
"""

RATE = 6.77

cnyAmountStr = input('请输入人民币(CNY)金额：')
cnyAmountFlt = eval(cnyAmountStr)


usdAmount = cnyAmountFlt / RATE

print('美元(USD)金额是：',usdAmount)
