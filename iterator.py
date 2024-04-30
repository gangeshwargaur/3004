t1=('a', 'b', 'c', 'd', 'e')
t1_iterator=iter(t1)
print("inside the loop")
for index,item in enumerate(t1_iterator):
    print(item)
    if index==2:
        break
print("outside the loop")
print(next(t1_iterator))
print(next(t1_iterator))
