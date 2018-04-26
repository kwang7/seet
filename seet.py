a = [1,2,3]
b = [2,3,4]

def intersection(a,b):
    return [x for x in a if x in b]

def set_difference(a,b):
    return [x for x in a if x not in b]



print intersection(a,b)
li1= set_difference(a,b)
li2= set_difference(b,a)
li1.append(li2)
print li1
