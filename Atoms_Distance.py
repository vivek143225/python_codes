import math
print("Hydrogen position")
a = int(input("Enter x1 : "))
b = int(input("Enter y1 : "))
c = int(input("Enter z1 : "))
print("carbon position")
d = int(input("Enter x2 : "))
e = int(input("Enter y2 : "))
f = int(input("Enter z2 : "))
print("nitrogen position")
g = int(input("Enter x3 : "))
h = int(input("Enter y3 : "))
i = int(input("Enter z3 : "))

j = math.sqrt((a - d)**2 + (b - e)**2 +(c - f)**2)
print("Distance Between Hydrogen to Carbon:",j)
k = math.sqrt((d - g)**2+(e - h)**2+(f - i)**2)
print("Distance Between Carbon to nitrogen:",k)
l = math.sqrt((a - g)**2+(b - h)**2+(c - i)**2)
print("Distance Between Nitrogen to Hydrogen",l)


