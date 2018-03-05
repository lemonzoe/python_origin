out=open("data.out","w")
# out——数据文件对象；data.out——所写文件的文件名；w——要使用的访问模式
print("Norwegian Bleues stun easily.",file=out)
out.close()
# 完成工作时，一定要关闭文件，确保所有数据都写至磁盘，这称为刷新输出（flushing）
# 使用访问模式w时，python会打开指定的文件来完成写。
# 如果这个文件已经存在，则会清空它现有的内容，也就是完全清除。
# 要追加到一个文件，需要使用访问模式a。
# 要打开一个文件来完成写和读（不清除），需要使用w+。
# 如果想打开一个文件完成写，但是这个文件并不存在，那么首先会为你创建这个文件，然后再打开文件进行写。
import os
os.chdir('d:/python_origin/d3/test/headfirst')
man=[]
other=[]
try:
    data=open('headfirst.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            line_spoken=line_spoken.strip()
            if role=='Man':
                man.append(line_spoken)
            elif role=='Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except  IOError:
    print('The datafile is missing!')
# 使用try/except来保护代码避免IOError
try:
    # 以写模式打开文件，分别赋至一个文件对象
    man_file=open('man_data.txt','w')
    other_file=open('other_data.txt','w')
    # 使用“print()”BIF将指定的列表保存在指定的磁盘文件
    print(man,file=man_file)
    print(other,file=other_file) # 假如是问题行:异常处理代码完成了任务，
                                 # 但是数据可能被破坏。需要保证不
                                 # 论是否出现一个IOError都会运行某些代码。
                                 # 在代码上下文中，希望无论如何要确保关闭文件。
    # 记得关闭文件
                                 # 因此一下两行代码需要转移至finally
    # man_file.close()
    # other_file.close()  
except IOError:
    print('File error.')
# 发现other_data.txt文件空白。
# 向文件写数据，如果在文件关闭前需要处理一个IOError，所写的数据可能会被破坏，
# 而且只有这种情况真正发生了才能知道，否则根本无法了解这样一点。
finally:
    man_file.close()
    other_file.close()
# 不论什么情况，finally组中的代码总会运行，可以确保文件妥善地关闭（即使出现写错误）