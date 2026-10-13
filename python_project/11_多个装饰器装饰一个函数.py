"""
多个装饰器装饰一个函数，是按照由内向外的顺序来装饰的，
但如果你要用装饰器的写法来做，看到的效果是：从上往下执行的

"""
#发表评论前，先登陆，在验证码
def check__login(fn_name):
    def fn_inner():
        print("校验登陆")
        fn_name()
    return fn_inner

def check_code(fn_name):
    def fn_inner():
        print("校验验证码")
        fn_name()
    return fn_inner


# @check__login   #语法糖： 从上往下执行的，先执行check__login，再执行check_code
# @check_code
def comment():
    print("发表评论")


comment=check__login(check_code(comment))  #等价于上面的语法糖,由内往外
comment()


