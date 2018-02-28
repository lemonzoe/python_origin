try:
    data=open('missing.txt')
    print(data.readline(),end='')
except IOError:
    print('File error')
# finally:
#     data.close()
# File error  ← 错误消息
# Traceback (most recent call last):
#   File "d:\python_origin\class3.py", line 7, in <module>
#     data.close()
# NameError: name 'data' is not defined
# ↑ 产生了另一个异常，导致代码崩溃。
# 文件不存在时，数据文件对象并未创建，这样就不可能在数据对象上调用close()方法，
# 所以最后会得到一个NameError错误。一种简便的修正方法是对finally组增加一个简单的测试，
# 尝试调用close()之前先查看data名是否存在。
# locals()BIF会返回当前作用域中定义的所有名的一个集合。
# 下利用这个BIF，只有在安全时才调用close()：
finally:
    if 'data' in locals():
        data.close()
# 在locals()BIF返回的集合中搜索字符串data。如果找到，
# 可以认为文件已经成功打开，可以安全地调用close()方法
# 如果出现其他错误（代码调用print()BIF时可能有问题），你的异常处理代码
# 会捕获到这个错误，显示“File error”消息，最后关闭所有打开的文件。 
try:
    data=open('missing.txt')
    print(data.readline(),end='')
except IOError as err: 
    # 为异常对象给定一个名
    print('File error: '+ str(err))
# str()BIF把异常对象转换为字符串
finally:
    if 'data' in locals():
        data.close()
# 以上是通常的“try/except/finally”模式。
# 使用“with”就不再需要“finally”组了
try:
    with open('its.txt',"w") as data:
        print("It's...",file=data)
except IOError as err:
    print('File error: ' + str(err))
finally:
    if 'data' in locals():
        data.close()
# 使用with时，不再需要操心关闭打开的文件。