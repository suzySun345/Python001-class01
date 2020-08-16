
def MyMap(func,data):
    res = []
    for x in data:
        res.append(func(x))
    return res

def func(x):
    return x*x

result = []
result = MyMap(func,[1,2,3,4,5])
for i in result:
    print(i)