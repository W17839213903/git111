import xlrd
from xlutils.copy import copy
f=xlrd.open_workbook('text.xls')
new_f=copy(f)
sheet=new_f.get_sheet(0)
with open('a.txt','r', encoding = 'utf-8') as f:
    a=f.readlines()
    print(a)
for i in a:
    b=i.split(',')
    print(b)
    for k in range(len(a)):
            sheet.write(k,0,b[0])
            sheet.write(k,1,b[1])
            sheet.write(k,2,b[2])
new_f.save('text.xls')
