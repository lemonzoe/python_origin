import os
os.chdir('d:/python_origin/d3/test/headfirst')
# 一定要记得切换目录
data=open('headfirst.txt')
for each_line in data:
    # (role,line_spoken)=each_line.split(':')
    # 遇到一句话有两个冒号的情况就会出错(16行)
    (role,line_spoken)=each_line.split(':',1)
    # 遇到没有冒号的行数出错(23行)
    print(role,end='')
    print(' said:',end='')
    print(line_spoken,end='')