def function1(func):
    def f1():
       print("before decotor1 calling")
       func()
       print("after decorator1 calling")
    return f1

def  function2(func):

    def f2():

       func()
       print("before decotor2 calling")
       print("after decorator2 calling")
    return f2

@function1
@function2
def say_hello():
    print("hi and hello")

say_hello()