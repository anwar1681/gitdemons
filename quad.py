
print("ax^2 +bx + c = 0")

a = int(input('enter value of a: '))
b = int(input('enter value of b: '))
c = int(input('enter value of c: '))

D = round((b**2 - 4*a*c)**0.5,2)
x1 = (-b + D)/(2*a)
x2 = (-b - D)/(2*a)

