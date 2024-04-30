def  f1(x):

    def f2(y):
        return x+y
    return f2

obj1=f1(12)
print(obj1(6))