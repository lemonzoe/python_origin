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
try:
    with open('man_data.txt','w') as man_file:
        print(man,file=man_file)
    with open('other_data.txt','w') as other_file:
        print(other,file=other_file)
    # 或 with open('man_data.txt','w') as man_file,open('other_data.txt','w') as other_file:
    # print(man,file=man_file)
    # print(other,file=other_file)
except IOError as err:
    print('File error: '+ str(err))
# 使用一个with语句打开数据文件，并显示其中的一行：
with open('man_data.txt') as mdf:
    print(mdf.readline())
#print( )会模仿python解释器实际存储列表数据的格式来显示数据。