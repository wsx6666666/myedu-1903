# 调用其他模块的方法

# 先导入模块  语法 : from 包名 import 模块名
from day01 import base_type

if __name__ == '__main__':
    # 使用 :  模块名.方法名(参数1,参数2)
    base_type.add_demo(5,10)
    value = base_type.jianfa_demo(3, 6)
    print(value)