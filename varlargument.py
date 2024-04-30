def function(*args,**kargs):
    print("positional argument")
    for arg in args:
        print(arg)
    print("keyword argument")
    for keys,values in kargs.items():
        print(f"{keys} : {values}")

function(1,2,3,4,name="alice",age=30)