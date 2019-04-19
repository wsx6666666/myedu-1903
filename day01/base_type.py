# def声明一个方法
# first_demo 这是方法名
# ():

def text1():
    print('text1')

def text2():
    print('text2')

def text3():
    print('text3')

def first_demo():
    print('xxx')
    print('jjj')

# 整数类型的演示
def int_demo():
    # 声明一个变量  = 前面的就是变量名   , =后面的就是变量值
    aint = 5
    # 打印 aint变量
    print(aint)
    # type(aint) : 获取aint的变量类型
    # print(type(aint)) : 打印 aint的变量类型
    print(type(aint))

# 字符串类型的演示
def str_demo():
    astr = '5'
    print(astr)
    print(type(astr))

# 小数类型的演示
def float_demo():
    afloat = 5.5
    print(afloat)
    print(type(afloat))

def type_zhuanhuan():
    aint = 7
    # 获取 aint 的类型
    print(type(aint))
    # 将aint 转换为 str 类型 , 在打印出它的类型
    print(type( str(aint) ))
    # 将aint 再转换回来:  int 类型 , 在打印出它的类型
    print(type( int(aint) ))

    # 被转换的字符 必须是满足 数字的格式
    # print(type( int('xxx') ))

# 字符串拼接
def str_join():
    a = 123
    b = '你好'
    c = 5.88
    # 方式一 : 将变量转换为str  然后用 + 连接起来
    print(str(a)+b+str(c))
    # 方式二 %s: 占位符
    print('a是%s b是%s c是%s'%(a,b,c))

# 加法方法演示  (a,b) :  () 里面的东西 叫参数,多个参数用 , 分隔开 ; 参数等同于变量 , 只不过没有赋值
def add_demo(a,b):
    print(a+b)

def jianfa_demo(a,b):
    c = a - b
    # return : 返回的意思  后面是什么  方法执行后就返回什么
    return c
    # return 后面不能继续写代码,因为方法执行到 return 就会结束
    #print(c)

if __name__ == '__main__':
    # text1()
    # print('hell')
    # first_demo()
    # int_demo()
    # str_demo()
    # float_demo()

    # 调用方法, 并传参
    # add_demo(3000,5832784)
    # 加法如果传字符串 ,会把两个字符串拼接到一起
    # add_demo('你好',' 世界')
    # type_zhuanhuan()
    # str_join()
    # 将减法执行完 返回的值 赋值 给 c   所以c是8
    c = jianfa_demo(6, 2)
    # d = 加法执行完返回的值, 但是 加法没有返回值   所以d 是 None
    d = add_demo(6,2)
    print(c)
    print(d)
    print(type(d))