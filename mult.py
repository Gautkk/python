def mul(x, y):
    if(x==1): 
        return y;
    if(x%2==1):
        print((x-1),y)
        return mul(x-1,y)+y;
    else:
        print(x/2,y+y)
        return mul(x/2,y+y);

print()
print("Multiplication Egyptienne")
print()
print("Saisie de x:")
x=int(input())
print("Saisie de y:")
y=int(input())

print()
print(mul(x,y));
   

