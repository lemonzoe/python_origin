# class3修正版本。
import os
os.chdir('d:/python_origin/d3/test/headfirst')
data=open('headfirst.txt')
for each_line in data:
    if not each_line.find(':')==-1:
        # 第一次见if not，简直我伙呆。一定要掌握这种反向逻辑关系。
        (role,line_spoken)=each_line.split(':',1)
        print(role,end='')
        print(' said:',end='')
        print(line_spoken,end='')
        # data.close()
        # 注意不能在for循环里写close()
        # ValueError: I/O operation on closed file.
data.close()
# 代码出问题，python解释器会显示一个traceback，后面跟着一个错误消息。
# 运行时错误叫做异常（exception）