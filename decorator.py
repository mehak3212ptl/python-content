def decorator(fun):
    def wrapper():
        print("start work")
        fun()
        print("stop work")
    return wrapper
def original_fun():
    print("this is mehak patel")
var=decorator(original_fun)
var()
