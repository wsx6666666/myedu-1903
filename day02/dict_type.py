
import json

# 全局变量
adict = {"username":"yansl","password":"123456"}
bdict = {'5':"yansl","password":[2,5]}

cdict_str = '{"username":"yansl","password":"123456"}'

# 查询字典中的元素
def dict_sel():
    # 通过key来访问,key可以是 str 类型 ,也可是int类型
    print(adict['username'])
    print(bdict[5])
    # 将访问到的值 可以重新赋值 给 新的变量
    b = bdict['password']
    print(b)

# 删除字典中的元素
def dict_del():
    adict.pop('password')
    print(adict)

# 更改字典中的值
def dict_update():
    adict['username'] = '闫松林'
    print(adict)

# 合并字典
def dict_add():
    # 方式一
    # 字典中的key 不能重复 , 相同key 保存value时 取 括号里面的值
    adict.update(bdict)
    print(adict)

    # 方式二
    # 使用 dict() 方法时 ,两个字典中的key 必须都是字符串格式
    cdict = dict(adict,**bdict)
    print(cdict)

# 增加字典中的元素
def dict_add1():
    adict['sex'] = '男'
    print(adict)

# 字典转换字符串  json.dumps()
def dict2str():
    print(type(adict))
    # 将 adict 转换成 字符串类型  再重新赋值 给 adict_str
    adict_str = json.dumps(adict)
    print(adict_str)
    print(type(adict_str))

# 字符串转换字典 json.loads()
def str2dict():
    print(type(cdict_str))
    # 将 cdict_str 转换成 字典类型  再重新赋值 给 cdict
    cdict = json.loads(cdict_str)
    print(cdict)
    print(type(cdict))

if __name__ == '__main__':
    # dict_sel()
    # dict_del()
    # dict_update()
    # dict_add()
    # dict_add1()
    # dict2str()
    str2dict()