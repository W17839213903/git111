from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

#创建窗口
window = Tk()   #不会显示
#窗口标题
window.title('hello')
#设置窗口大小
window.geometry('400x400')
#定义文本标签
wd = Label(window,text='你好',font=('微软雅黑',20))
#把标签放到
#显示窗口
window.mainloop()
