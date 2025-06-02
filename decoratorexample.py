def decoratorexample(func):
    def wrapper(*args,**kwargs):
        print(f"calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        res= func(*args,**kwargs)
        return res
    return wrapper

@decoratorexample
def divion(a,b):
    return a/b
# print(divion(10,2))

import functools

users={
    'name':'karthikeya',
    'isauthenticated':False
}

def bankaccountdec(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        if not users['isauthenticated']:
            print("Access denied")
        return func(*args,**kwargs)
    return wrapper

@bankaccountdec
def withdraw(money):
    print(f"{money} is successfully withdrawn.")

withdraw(1000)

users['isauthenticated']=True

withdraw(2000)