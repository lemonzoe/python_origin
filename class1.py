import os
os.chdir('d:/python_origin/d3/test/headfirst')
man=[]
other=[]
# 为“man”和“other”分别赋一个空列表。
try:
    data=open('headfirst.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            line_spoken=line_spoken.strip()
            # 将去除空白符后的字符串再赋回到自身。
            # “strip()”方法从字符串中去除不想要的空白符。
            # 以下根据是谁讲的话来更新其中一个列表。
            if role=='Man':
                man.append(line_spoken)
            elif role=='Other Man':
            # elif=else if
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except  IOError:
    print('The datafile is missing!')
# 最后在屏幕上显示处理后的数据
print(man)
print(other)