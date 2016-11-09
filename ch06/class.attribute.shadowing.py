class Point():
    x = 10
    y = 7

p = Point()
print(p.x) # 10
print(p.y) # 7

p.x = 12 # p gets its own 'x' attribute
print(p.x) # 12
print(Point.x) # 10

del p.x # delete instance sttribute
print(p.x) # 10

p.z = 3 # let's make it a 3D point
print(p.z) # 3

print(Point.z)
# AttributeError: type object 'Point' has no attribute 'z'
