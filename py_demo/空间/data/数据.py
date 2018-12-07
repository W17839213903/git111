import xlrd

def duqu():
    f=xlrd.open_workbook(r'C:\Users\bigbaby\Desktop\空间.xlsx')
    sheet = f.sheets()[0]
    hang = sheet.nrows
    a=[]
    for i in range(1,hang):
        aa = sheet.row_values(i)
        a.append(aa)
    return a
