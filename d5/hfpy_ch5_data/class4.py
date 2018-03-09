# 创建一个函数，从各列表接受一个字符串作为输入
# 然后处理这个字符串，将找到的所有短横线或冒号替换为一个点号
# 返回清理过的字符串（如果字符串已经包含一个点号，则不需要再清理）
def sanitize(time_string):
    # 使用in操作符检查字符串是否包含一个短横线或冒号
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
        # 如果字符串不需要清理，就什么也不做
    (min,secs)=time_string.split(splitter)
    # 分解字符串
    return(min+'.'+secs)
# 迭代处理每一个数据列表
with open('james.txt') as jaf:
    data=jaf.readline()
james=data.strip().split(',')
with open('julie.txt') as juf:
    data=juf.readline()
julie=data.strip().split(',')
with open('mikey.txt') as mif:
    data=mif.readline()
mikey=data.strip().split(',')
with open('sarah.txt') as saf:
    data=saf.readline()
sarah=data.strip().split(',')
# 创建空的新列表
clean_james=[]
clean_julie=[]
clean_mikey=[]
clean_sarah=[]
# 取原列表中的各个数据项进行清理，追加到新列表
for each_t in james:
    clean_james.append(sanitize(each_t))
for each_t in julie:
    clean_julie.append(sanitize(each_t))
for each_t in mikey:
    clean_mikey.append(sanitize(each_t))
for each_t in sarah:
    clean_sarah.append(sanitize(each_t))
# 显示已排序的新列表
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
# 默认地，sort( )方法与sorted( )BIF都会按升序对数据进行排序。
# 要以降序排序，则需要向sort( )或sorted( )传入参数reverse=True。