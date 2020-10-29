#function returning function(name)

def decoratorFn(func):
    def wrapper():
        print("......before......")
        func()
        print("......after.......")
    return wrapper

def simpleFn():
    print("My function")

newFn = decoratorFn(simpleFn)
newFn()


'''
def decoratorFn(func):
    def wrapper():
        print("......before......")
        func()
        print("......after.......")
    return wrapper


@decoratorFn
def simpleFn():
    print("My function")

simpleFn()
'''