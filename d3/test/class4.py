each_line="I tell you, there's no such thing as a flying circus"
h=each_line.find(':')
print(h)
# 字符串不包含冒号，返回-1表示未找到
the_file="I tell you: there's no such thing as a flying circus"
p=the_file.find(':')
print(p)
# 字符串包含一个冒号，返回一个正的索引值