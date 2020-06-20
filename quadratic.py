#program to find roots of equation a**x+b*x+c
print("Equation: ax^2 + bx + c ")

#Take Input a,b,c from user
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))

#calculate discriminant d
d=b**2-4*a*c
d1=d**0.5

#if the value of d < 0 then print roots are imaginary
if(d<0):
    print("The roots are imaginary. ")

#print the roots to two decimal places
else:
    r1=(-b+d1)/2*a
    r2=(-b-d1)/2*a
    print("The first root: ",round(r1,2))
    print("The second root: ",round(r2,2))
