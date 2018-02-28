# 导入os模块（默认模块）,只有默认模块才能运行os.getcwd()
import os
p=os.getcwd()
print(p)
# 输出当前目录
os.chdir('d:/python_origin/d3/test/headfirst')
# 切换目录
o=os.getcwd()
print(o)
# 打开数据文件
data=open('headfirst.txt')
print(data.readline(),end='')
print(data.readline(),end='')
# 使用readline()方法从文件获取一个数据行，然后输出数据
data.seek(0)
# 用seek()方法返回到文件起始位置。对python的文件也可以使用tell()
for each_line in data:
    print(each_line,end='')
# 输出每一行数据
data.close()
# 处理完文件之后，一定要关闭