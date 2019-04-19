# 元组类型  tuple
# 与list的区别 : 只能被访问,不能更改

if __name__ == '__main__':
    atuple = (1,5,6,'ha',6)
    print(atuple[2])
    print(atuple[2:4])
    atuple[2] = 7