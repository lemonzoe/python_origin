def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    (min,secs)=time_string.split(splitter)
    return(min+'.'+secs)
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
# 排序和清理各个列表
james=sorted([sanitize(t) for t in james])
julie=sorted([sanitize(t) for t in julie])
mikey=sorted([sanitize(t) for t in mikey])
sarah=sorted([sanitize(t) for t in sarah])
# 删除重复的数据项
unique_james=[]
for each_t in james:
    if each_t not in unique_james:
        unique_james.append(each_t)
print(unique_james[0:3])
# 创建空列表存放唯一的数据项
unique_julie=[]
# 在现有的数据上迭代处理
for each_t in julie:
    # 如果这个数据项还不在新列表中
    if each_t not in unique_julie:
        # 将这个唯一的数据项追加到新列表中
        unique_julie.append(each_t)
# 从列表分片得到前三个数据项
print(unique_julie[0:3])
unique_mikey=[]
for each_t in mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)
print(unique_mikey[0:3])
unique_sarah=[]
for each_t in sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)
print(unique_sarah[0:3])