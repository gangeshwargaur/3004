import copy

l1=[1,2,[3,4],5,6,7]
l2=copy.copy(l1)
l2[2][1]=9
l3=copy.deepcopy(l1)
l3[2][1]=10
print("====================================================================")
print("id of l1 ",id(l1),"value of l1",l1)
print("====================================================================")
print("id of l2 ",id(l2),"value of l2",l2)
print("====================================================================")
print("id of l3 ",id(l3),"value of l3",l3)
print("====================================================================")
print("id of l1 ",id(l1),"value of l1",l1)
