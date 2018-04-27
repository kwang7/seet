#Kelly Wang Jennifer Zhang
#SoftDev2 pd7
#K16 Ready, Set, Math!
#2018-04-26


a = [1,2,3]
b = [2,3,4]

def intersection(a,b):
    return [x for x in a if x in b]

def set_difference(a,b):
    return [x for x in a if x not in b]

def union(a,b):
    return set_difference(a,b) + set_difference(b,a) + intersection(a,b)

def sym_diff(a,b):
    return set_difference( union(a,b) , intersection(a,b) )

def cart_prod(a,b):
    return  [ (x,y) for x in a for y in b ]
    
print intersection(a,b)
print set_difference(a,b)
print union(a,b)
print sym_diff(a,b)
print cart_prod(a,b)
