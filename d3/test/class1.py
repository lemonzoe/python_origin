the_file=open('test01.txt')
p=the_file.read()
print(p)
the_file.close()
# 注意close后面的()
# 注意当前的工作目录，否则查询不到open的文件，则会出现FileNotFoundError。