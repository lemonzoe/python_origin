"""
with open('1.pickle','wb') as savedata:
    pickle.dump([1,2,'three'],savedata)
    ...
with open('1.pickle','rb') as restoredata:
    a_list=pickle.load(restoredata)  # 使用load()恢复数据。
print(a_list)
"""
# 保存数据 dump()
import pickle
# 一定要导入pickle模块
try:
    with open('man_data.txt','wb') as man_file,open('other_data.txt','wb') as other_file:
        # "b"告诉python以二进制模式打开数据文件
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)
        # 保存数据，使用dump()
except IOError as err:
    print('File error: '+str(err))
except pickle.PickleError as perr:
    print('Pickling error: '+str(perr))
# 恢复数据load()
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

# 第四章笔记
# strip()方法可以从字符串去除不想要的空白符
# print()BIF的file参数控制将数据发送/保存到哪里
# finallly组总会执行，而不论try/except语句中出现什么异常
# 会向except组传入一个异常对象，并使用as关键字赋至一个标识符
# str()BIF可以用来访问任何数据对象（支持串转换）的串表示
# locals()BIF返回当前作用域中的变量集合
# in操作符用于检查成员关系
# “+”操作符用于字符串时将连接两个字符串，用于数字则会将两个数相加
# with语句会自动处理所有已打开文件的关闭工作，即使出现异常也不会例外。with语句也使用as关键字
# sys.stdout是python中所谓的“标准输出”，可以从标准库的sys模块访问
# 标准库的pickle模块允许容易而高效地将python数据对象保存到磁盘以及从磁盘恢复
# pickle.dump()函数将数据保存到磁盘
# pickle.load()函数从磁盘恢复数据