"""
案例：演示带参数的装饰器

1个装饰器的参数有且只有1个
如果装饰器有多个参数，可以在装饰器外边在包裹一层，把装饰器当作内部函数返回即可

"""

#一个即能装饰加法又能装饰减法的装饰器，即带参数的装饰器·
# def my_decorator(fn_name):
#     def fn_inner(a,b):
#         print("计算中。。。。")
#         return fn_name(a,b)
#     return fn_inner

# @my_decorator
# def get_sum(a,b):
#     return a+b


# @my_decorator
# def get_sub(a,b):
#     return a-b



def my_decorator(fn_name):
    def fn_inner(a,b):
        if fn_name.__name__=="get_sum":
            print("计算加法")
        elif fn_name.__name__=="get_sub":
            print("计算减法")
        return fn_name(a,b)
    return fn_inner

@my_decorator
def get_sum(a,b):
    return a+b


@my_decorator
def get_sub(a,b):
    return a-b

# def flag_fn(flag):                  
#     def my_decorator(fn_name):
#         def fn_inner(a,b):
#             if flag=="+":
#                 print("计算加法")
#             elif flag=="-":
#                 print("计算减法")
#             return fn_name(a,b)
#         return fn_inner
#     return my_decorator

# @flag_fn("+")
# def get_sum(a,b):
#     return a+b


# @flag_fn("-")
# def get_sub(a,b):
#     return a-b




print(get_sub(10,5))
print("-"*10)
print(get_sum(1,2))
