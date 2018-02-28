movies=[
     "the holy grail",1975,"terry jones&terry gilliam",91,
         ["graham chapman",
             ["michael palin","john cleese","terry gilliam","eric idle","terry jones"]]]
print(movies[4][1][3])
print(movies)
for each_item in movies:
    print(each_item)
# 显示嵌套列表
for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)
# 只显示一个嵌套
for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            if isinstance(nested_item,list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)
# 可以将循环语句变为一个函数，使代码更精简