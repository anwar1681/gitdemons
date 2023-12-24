
print("ax^2 +bx + c = 0")
def quad():
   
    a = int(input('enter value of a: '))
    b = int(input('enter value of b: '))
    c = int(input('enter value of c: '))

    D = round((b**2 - 4*a*c)**0.5,2)
    x1 = round((-b + D)/(2*a),2)
    x2 = round((-b - D)/(2*a),2)

    print('First root x1: ',x1)
    print('Second root x2: ',x2)

# if __name__=="__main__":
quad() 