# 设定缩进默认值
def print_lol(the_list,indent=False,level=0): 
# 默认indent的缺省值为false
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1)
            # 签名已经改变，所以要更新调用
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='')
            print(each_item)
names=['rng','we',['im','blg'],'edg',['fpx']]
print_lol(names)
print_lol(names,True)
print_lol(names,True,4)