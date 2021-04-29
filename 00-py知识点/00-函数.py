def print_info():
    print('函数一')


def print_info_param(param):
    print('函数二' + param)


def ctof(c):
    f = c * 1.8 + 32
    return f

c = float(input('请输入摄氏温度：'))
print('华氏温度为：%5.1f°' % ctof(c))

# 不定参函数
def func1(*params):
    return sum(params)

print('2个参数：4+5=%d' % func1(4, 5))
print('3个参数：4+5*4 = %d' % func1(4, 5, 4))

# 全局变量
var1 = 10
var2 = 20

def scope():
    global var1
    # 局部变量
    var1 = 1
    var2 = 2
    print(var1, var2)

scope()
print(var1, var2)