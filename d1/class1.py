print ("hello,world!") 
print ("你好，世界")

movies=["the holy grail","the life of brian","the meaning of life"]
print(movies[2])
print(len(movies))
movies.append("omg")
# 增加尾项数据
print(movies)
movies.pop()
# 删除尾项数据
print(movies)
movies.extend(["edg","rng"])
# 列表末尾增加一个集合
print(movies)
movies.remove("edg")
# 移除特定项 
print(movies)
movies.insert(1,"ojbk")
# 在编号为1的槽前面增加一个数据项
print(movies)
fav_movies=["we","rng"]
# print(fav_movies[0])
# print(fav_movies[1])
for each_flick in fav_movies:
    print(each_flick)
count=0
while count<len(movies):
    print(movies[count])
    count=count+1
for each_flick in movies:
    print(each_flick)
# list() 这是一个工厂函数，创建一个新的空列表
# range()返回一个迭代器，根据需要生成一个指定范围的数字
# enumerate()创建成对数据的一个编号列表，从0开始
# int()将一个字符串或另一个数转换为一个整数（如果可行）
# id()返回一个python数据对象的唯一标识
# next()返回一个可迭代数据结构（如列表）中的下一项
for num in range(4):
    print(num)
# 生成直到（但不包括）4的数字