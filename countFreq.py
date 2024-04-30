def countFreq(l1):
    d1={}
    for ele in l1:
        if ele in  d1:
            d1[ele]+=1
        else:
            d1[ele]=1
    for keys , values in  d1.items():
        print("%d : %d"  %(keys,values))

if __name__=="__main__":
    l1=[1,1,1,2,2,3,3,3,4,4]
    countFreq(l1)
