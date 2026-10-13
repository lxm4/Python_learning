"""
闭包的语法：
    在函数嵌套的前提下，
    内层函数引用了外层函数的变量，
    并且外层函数返回了内层函数，
    这样的结构就形成了闭包。

#外部函数
def 外部函数名（外部参数）：
    #内部函数
    def 内部函数名（内部参数）：
        #使用外部函数的变量
    #返回内部函数
    return 内部函数名   #函数名和函数名（）是两个概念，前者表示函数对象，后者表示函数调用，
                        返回值是函数的返回值。

nonlocal关键字：
    nonlocal关键字用于在内部函数中修改外部函数的变量。

装饰器的作用：
    装饰器的作用是为函数或方法添加额外的功能，而不需要修改其源代码。它们通常用于日志记录、
    访问控制、缓存、性能测量等场景。装饰器本质上就是一个闭包函数。

"""
def make_multiplier(n):
    def multiplier(x):
        return x * n  # 引用了外层函数的变量 n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15



def log_call(func):
    """装饰无参无返回值的函数。"""
    def wrapper():
        print("函数开始执行")
        func()
        print("函数执行结束")
    return wrapper


@log_call
def say_hello():
    print("你好，Python！")


say_hello()


def log_call_with_args(func):
    """装饰有参数、无返回值的函数。"""
    def wrapper(name):
        print("准备问候")
        func(name)
    return wrapper


@log_call_with_args
def greet(name):
    print(f"你好，{name}！")


greet("小明")


def log_return_value(func):
    """装饰有参数、有返回值的函数。"""
    def wrapper(a, b):
        result = func(a, b)
        print(f"函数返回值：{result}")
        return result
    return wrapper


@log_return_value
def add(a, b):
    return a + b


total = add(3, 5)
print(f"计算结果：{total}")


# c = counter()()
# print(c)  # 1
# print(c)  # 1
# print(c())  # 1
# print(c())  # 2
# print(c())  # 3
# print(c())  # 4