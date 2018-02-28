# 一、增加错误检查代码
# 使用额外的逻辑来处理文件I/O错误
import os
os.chdir('d:/python_origin/d3/test/headfirst')
# 检查文件存在
if os.path.exists('sketch.txt'):
    # 需要保护的代码
    data=open('sketch.txt')
    for each_line in data:
        if not each_line.find(':')==-1:
            (role,line_spoken)=each_line.split(':',1)
            print(role,end='')
            print(' said: ',end='')
            print(line_spoken,end='')
    data.close()
else:
    # 通知用户消息
    print('The data file is missing!')
# 二、增加一层异常处理————try语句
# 使用另一个try语句来处理文件I/O错误
try:
    data2=open('headfirst.txt')
    for each_line in data2:
        try:
            (role,line_spoken)=each_line.split(':',1)
            print(role,end='')
            print(' said: ',end='')
            print(line_spoken,end='')
        # except: 会悄无声息地忽略运行时错误
        # 故改为以下指定要处理的运行时错误类型：
        except ValueError:
            pass
    data2.close()
# except: 会悄无声息地忽略运行时错误。改为：
except IOError:
    print('The data file is missing!')

# 第三章笔记：
# 1、使用open()BIF打开一个磁盘文件，创建一个迭代器从文件读取数据，一次读取一个数据行。
# 2、readline()方法从一个打开的文件读取一行数据。
# 3、seek()方法可以用来将文件“退回”到起始位置。
# 4、close()方法关闭一个之前打开的文件。
# 5、split()方法可以将一个字符串分解为一个子串列表。
# 6、Python中不可改变的常量列表成为元组(tuple)。一旦将列表数据赋至一个元组，就不能再改变。元组是不可改变的。
# 7、数据不符合期望的格式时会出现ValueError。
# 8、数据无法正常访问时会出现IOError（例如，可能你的数据文件已经被移走或者重命名）。
# 9、help()BIF允许你在IDLE shell中访问python的文档。
# 10、find()方法会在一个字符串中查找一个特定子串。
# 11、not关键字将一个条件取反。
# 12、try/except语句提供了一个异常处理机制，从而保护可能导致运行时错误的某些代码行。
# 13、pass语句就是python的空语句或null语句，它什么也不做。