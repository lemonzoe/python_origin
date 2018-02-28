movies=[
     "the holy grail",1975,"terry jones&terry gilliam",91,
         ["graham chapman",
             ["michael palin","john cleese","terry gilliam","eric idle","terry jones"]]]
# 这是一个模块，提供了一个名为print_lol的函数，函数的作用是打印列表，其中有可能包含（可能不包含）嵌套列表。
def print_lol(the_list,level): 
# 这个函数取一个位置参数，名为“the_list”,这可以是任何python列表（也可以是包含嵌套列表的列表）。
# 所指定的列表中的每个数据项会（递归地）输出到屏幕上，各数据项各占一行。
# 第二个参数用来在遇到嵌套列表时插入制表符。             
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level+1)
        else:
            for tab_stop in range(level):
                # 使用level的值来控制使用多少歌制表符
                print("\t",end='')
                # 每一层缩进显示一个tab制表符
            print(each_item)
# 以上是模块。以下调用模块
print_lol(movies,0)
# print_lol(movies) ——在定义函数时 level=0
# print_lol(movies,2)——缺省值为2，缩进从2开始
# print_lol(movies,-9)
