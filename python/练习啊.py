# class Hanshu():
#     def jiujiu(a):
#         for i in range(1,a):
#             for j in range(1,i+1):
#                 print('{}*{}={}'.format(j,i,i*j),end='\t')
#             print()
#     jiujiu(10)
#
#     def zonghe(a):
#         b=0
#         for i in range(1,a):
#             b+=i
#         print(b)
#     zonghe(101)
#
#     def zhishu(a):
#         b=0
#         for i in range(2,a):
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 b+=i
#         print(b)
#     zhishu(101)
#
#     def jiecheng(a):
#         b=1
#         c=0
#         for i in range(1,a+1):
#             b*=i
#             c+=b
#         print(c)
#     jiecheng(5)
#
#     def sanjiao():
#         a=input('<<<<')
#         b=a.split(',')
#         c=[]
#         for i in b:
#             if i not in c:
#                 c.append(int(i))
#         c.sort()
#         if c[0]+c[1]>c[2]:
#             if c[0]**2+c[1]**2==c[2]**2:
#                 print('直角三角形')
#             elif c[0]**2+c[1]**2<c[2]**2:
#                 print('钝角三角形')
#             else:
#                 print('锐角三角形')
#     sanjiao()
#
#     def caishuzi():
#         import random
#         a=random.randrange(1,10)
#         for i in range(1,4):
#             b=int(input('大抽奖'))
#             if b==a:
#                 print('真牛，中大奖啦')
#                 break
#             elif i==3:
#                 print('都不对，你真菜啊')
#             elif b>a:
#                 print('大了，你还有{}次机会'.format(3-i))
#             else:
#                 print('小了，你还有{}次机会'.format(3-i))
#     caishuzi()
#
#     def pingjun():
#         while True:
#             a=input('请输入一组数字')
#             b=a.split(',')
#             c=[]
#             if a == 'exit':
#                 break
#             for i in b:
#                 if i not in c:
#                     c.append(int(i))
#             print(sum(c)/len(c)  )
#             for j in c:
#                 if j < sum(c)/len(c):
#                     print(j)
#     pingjun()

# def zi():
#     a=input('<<<')
#     b=a[::-1]
#     s=0
#     for i,j in enumerate(b):
#         for h in range(10):
#             if str(h)==j:
#                 s+=h*10**i
#     print(s)
#     print(type(s))
# zi()
def zi():
    a=input('>>')
    b=a.split(',')
    c=[]
    for i in b:
        if int(i) not in c:
            c.append(int(i))
    print(c)
    print(type(c[0]))
zi()