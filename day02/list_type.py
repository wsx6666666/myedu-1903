
# 查询或者获取list 里面的值(元素)
# a[索引]: 或者叫下标值  元素从0开始数
def list_sel(a):
    # 顺序取值: 从0开始数
    print( a[2] )
    # 倒序取值: 从 -1 开始数
    print(a[-1])
    # 切片取值 语法: 前索引值 : 后索引值  取的时候取到后索引值的前一位
    print(a[2:5])
    print(a[0:2])
    # 不填值的话  从第一个开始取值
    print(a[:4])
    # 不填值的话  取到最后一位
    print(a[3:])

def list_del():
    # 定义一个list
    alist = ['a', 4, 'nihao', '8', '就是', '哈']
    # 调用删除方法 不填参数 默认删除最后一位
    alist.pop()
    print(alist)
    # 调用删除方法, 填写参数: 索引值   就可以删除指定元素
    alist.pop(0)
    print(alist)

    # 将切片获取的 元素 重新定义一个list 保存起来
    blist = alist[:-3]
    print(blist)

def list_add():
    alist = ['a', 4, 4, 4, 'nihao', '8', '就是', '哈']
    # 增加元素 ,增加在末尾
    alist.append('哈哈哈哈')
    print(alist)

    blist = [1,2,3]
    # 将一个list 作为元素,添加到 list里面
    alist.append(blist)
    print(alist)

    # 元素更换位置

# 更改list中的元素
def list_update():
    alist = ['a', 4, 'nihao', '8', '就是', '哈', '哈哈哈哈', [1, 2, 3]]
    alist[0] = 5
    print(alist)



if __name__ == '__main__':
    alist = ['a',4,'nihao','8','就是','哈']
    # list_sel(alist)
    # print(alist)
    # list_del()
    # list_add()
    list_update()