# def getcwd():
#    print("1111111")
the_file=open('test01.txt')
p=the_file.read()
print(p)
the_file.close()
# 注意close后面的()。否则FileNotFoundError: [Errno 2] No such file or directory: 'test01.txt'