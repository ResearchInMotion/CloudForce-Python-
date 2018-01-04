x,y,z,a,b,c=int(input("Number1 ")),int(input("Number2 ")),int(input("Number3 ")),int(input("Number4 ")),int(input("Number5 ")),int(input("Number6 "))
Sum=x+y+z+a+b+c
average=(x+y+z+a+b+c/5)
if(x>y) and (x>z) and (x>a) and (x>b) and (x>c):
    print("x is bigger")
elif (x<y) and (y>z) and (y>a) and (y>b) and (y>c):
    print("y is bigger")
elif(x<z) and (y<z) and (z>a) and (z>b) and (z>c):
    print("z is bigger")
elif(x<a) and (y<a) and (z<a) and (a>b) and (a>c):
    print("a is bigger")
elif(x<b) and (y<b) and (z<b) and (a<b) and (b>c):
    print("b is bigger")
elif(x<c) and (y<c) and (z<c) and (c>b) and (a<c):
    print("c is bigger")

print("the sum is ",Sum)
print("The average is ",average)