def func2(z):
    q=z+10
    return q
def func1(x):
    z=x+5
    p=func2(z)
    return p
x=5
y=func1(x)
print(y)
