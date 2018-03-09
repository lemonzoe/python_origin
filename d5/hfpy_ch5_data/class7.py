"""
# python中集合最突出的特性是集合中的数据项是无序的，且不允许重复。
# 如果要向一个集合增加一个数据项，而集合中已经包含有这个数据项，则python会将其忽略。
# 使用set()BIF创建一个空集合，并赋至一个变量
distances=set()
# 也可以一步完成集合的创建和填充
# 可以在大括号之间提供一个数据列表，或指定一个现有列表作为set()BIF的参数，这就是工厂函数
distances={10.6,11,8,10.6,"two",7}
distances=set(james)
# 工厂函数：用于创建某种类型的新的数据项
# 例如，“set()”就是一个工厂函数，因为它会创建一个新的集合
"""
def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    (mins,secs)=time_string.split(splitter)
    return(mins+'.'+secs)
# 创建一个新函数，接受一个文件名作为唯一的参数
def get_coach_data(filename):
    # 增加异常处理代码
    try:
        # 打开文件，读取数据
        with open(filename) as f:
            data=f.readline()
        # 将数据返回到代码之前先对数据完成分解/去除空白符处理
        return(data.strip().split(','))
    except IOError as ioerr:
        # 通知错误，并返回none指示失败
        print('File error:'+str(ioerr))
        return(None)
# 调用函数
james=get_coach_data('james.txt')
julie=get_coach_data('julie.txt')
mikey=get_coach_data('mikey.txt')
sarah=get_coach_data('sarah.txt')
print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])

# 第五章笔记
# 1.原地排序——转换然后替换
# 复制排序——转换然后返回
# 方法串链——从左向右读，对数据应用一组方法
# 函数串链——从右向左读，对数据应用一组函数
# 列表推导——在一行上制定一个转换（非迭代）
# 分片——从一个列表访问多个列表项
# 集合——一组无序的数据项，其中不包含重复项
# 2.sort()方法可以在原地改变列表的顺序
# sorted()BIF通过提供复制排序可以对几乎任何话数据结构排序
# 3.向sort()或sorted()传入reverse=True可以按降序排列数据
# 对以下代码：
# new_l=[]
# for t in old_l:
#     new_l.append(len(t))
# 使用列表推导重写这个代码：
# new_l=[len(t) for t in old_l]
# 4.要访问一个列表中的多个数据项，可以使用分片：
# 例如： my_list[3:6]
# 这会访问列表中从索引位置3直到（但不包括）索引位置6的列表项。
# 5.使用set()工厂方法可以创建一个集合。