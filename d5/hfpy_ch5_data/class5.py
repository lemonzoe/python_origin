"""
# 创建一个新列表来存放转换后的数据
clean_mikey=[]
# 迭代处理原列表中的各个数据项
for each_t in mikey:
    # 每次迭代时完成转换
    # 将转换后的数据追加到新列表
    clean_mikey.append(sanitize(each_t))
# 转换为以下代码
clean_mikey=[sanitize(each_t) for each_t in mikey]
# 不需要append()方法，因为这个动作已经隐含在列表推导中
"""
def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    (min,secs)=time_string.split(splitter)
    return(min+'.'+secs)
# 分钟转换为秒
mins=[1,2,3]
secs=[m*60 for m in mins]
print(secs)
# 米转换为英尺
meters=[1,10,3]
feet=[m*3.281 for m in meters]
print(feet)
# 给定包含混合大小写字符串的列表，转换为全大写的字符串
lower=['I',"don't",'like','spam']
upper=[s.upper() for s in lower]
print(upper)
# sanitize()函数
dirty=['2-22','2:22','2.22']
clean=[sanitize(t) for t in dirty]
print(clean)
# 将一个字符串列表转换为一个浮点数列表，替换原来的列表数据
clean=[float(s) for s in clean]
print(clean)
# 转换还可以是一个函数链
# 支持合并对数据项的转换
clean=[float(sanitize(t)) for t in ['2-22','3:33','4.44']]
print(clean)
# 列表推导与列表迭代
# 如果必须对一个列表中的每一项完成一个转换，使用列表推导是上策
# 特别是如果能很容易地在一行上指定转换（或指定为一个函数链），列表推导尤其适用
# 列表迭代可以完成列表推导所能完成的全部工作，只是代码量多一些
# 但迭代确实能提供更大的灵活性


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
print(sorted([sanitize(t) for t in james]))
print(sorted([sanitize(t) for t in julie]))
print(sorted([sanitize(t) for t in mikey]))
print(sorted([sanitize(t) for t in sarah]))
# 定义列表推导时,千万别使用函数链sort(sanitize(t))。
# 这个栗子,sorted()BIF希望对一个系列表排序，而不是针对单个数据项