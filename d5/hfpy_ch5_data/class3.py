# 对数据使用复制排序
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
print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))
# 可见数据排序出错。数据中存在的不一致性导致排序失败。
# python可以对字符串排序，排序时，短横线排在点号前面，点号在冒号前面。