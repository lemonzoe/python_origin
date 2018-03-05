import os
os.chdir('d:/python_origin/d3/test/headfirst')
data=open('headfirst.txt')
for each_line in data:
    try:
        (role,line_spoken)=each_line.split(':',1)
        print(role,end='')
        print(' said:',end='')
        print(line_spoken,end='')
    except:
        pass
data.close()