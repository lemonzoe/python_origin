import os
os.chdir('d:/python_origin/d3/test/headfirst')
import sys
man=[]
other=[]
def print_lol(the_list,indent=False,level=0,fn=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fn)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='',file=fn)
            print(each_item,file=fn)
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
        print_lol(man,fn=man_file)
    with open('other_data.txt','w') as other_file:
        print_lol(other,fn=other_file)
except IOError as err:
    print('File error: '+ str(err))
import pickle
try:
    with open('man_data.txt','wb') as man_file,open('other_data.txt','wb') as other_file:
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)
except IOError as err:
    print('File error: '+str(err))
except pickle.PickleError as perr:
    print('Pickling error: '+str(perr))
import pickle
new_man=[]
try:
    with open('man_data.txt','rb') as man_file:
        new_man=pickle.load(man_file)
except IOError as err:
    print('File error: '+ str(err))
except pickle.PickleError as perr:
    print('Pickling error: '+ str(perr))
print_lol(new_man)