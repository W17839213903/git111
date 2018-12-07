
import xlrd


def duqu():
    shuju = []
    f = xlrd.open_workbook(r'C:\Users\bigbaby\Desktop\最近\表格\wangdabao.xls')
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(1,num):
        aaa = sheet.row_values(i)
        shuju.append(aaa)
    # print(shuju)
    return shuju
duqu()