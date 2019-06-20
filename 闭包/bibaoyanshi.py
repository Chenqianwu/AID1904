def mul():
    return([lambda x:i*x for i in range(4)])
print([m(2) for m in mul()])


def mul():
    list=[]
    for i in range(4):
        def lam(x):
            return i*x
        list.append(lam)
    return list
print([m(2) for m in mul()])

def mul():
    list=[]
    for i in range(4):
        def lam(x,n=i):
            return n*x
        list.append(lam)
    return list
print([m(2) for m in mul()])