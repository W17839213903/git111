

#从表格到txt

#
# import xlrd
# biao = xlrd.open_workbook('text1.xls')   # 打开一个表格
# txt=open('b.txt','w',encoding='utf-8')    #打开一个文件
# sheet=biao.nsheets     #获取有多少标签页
# sheet=biao.sheets()[0]  #索引获取标签页
# lie=sheet.ncols      #统计多少列
# hang=sheet.nrows      #统计多少行
# for i in range(hang):    #循环显示每一行的内容
#     aa = sheet.row_values(i)
#     for j in range(lie):
#         if j == lie-1:
#             txt.write('{}'.format(aa[0])+' ')
#             txt.write('{}'.format(aa[1])+' ')
#             txt.write('{}'.format(aa[2])+'\n')
#
#





# import xlrd
# biao = xlrd.open_workbook('text1.xls')
# txt = open('a.txt','w',encoding='utf-8')
# bq = biao.nsheets
# bq = biao.sheets()[0]
# aa = bq.nrows
# bb = bq.ncols
# for i in range(aa):
#     hang = bq.row_values(i)
#     print(hang[0],hang[1],hang[2])
#     for j in range(bb):
#         if j == bb-1:
#             txt.write('{}'.format(hang[0]))
#             txt.write('{}'.format(hang[1]))
#             txt.write('{}'.format(hang[2])+'\n')