# # # # # # # # #
# CNY/汇率 = USD
# # # # # # # # #

cnyAmountStr = input('请输入人民币(CNY)金额：')
cnyAmountFlt = eval(cnyAmountStr)

rate = 6.77

usdAmount = cnyAmountFlt / rate

print('美元(USD)金额是：',usdAmount)
