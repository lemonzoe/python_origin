# 打开文件
with open('james.txt') as jaf:
    # 读数据行
    data=jaf.readline()
# 将数据转换为一个列表    
james=data.strip().split(',')
# 方法串链。去除字符串中所有空白符后，处理并创建新列表。
with open('julie.txt') as juf:
    data=juf.readline()
julie=data.strip().split(',')
with open('mikey.txt') as mif:
    data=mif.readline()
mikey=data.strip().split(',')
with open('sarah.txt') as saf:
    data=saf.readline()
sarah=data.strip().split(',')
# 显示列表
print(james)
print(julie)
print(mikey)
print(sarah)