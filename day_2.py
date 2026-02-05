#This program is of area of circle
PI=3.14
radius=float(input("Enter the value of r:"))
area=PI*radius*radius
print("The area of circle=",area)


#This is a second method to find area of circle
r=int(input("Enter the value of r:="))
print("The area of circle is :",3.14*r*r)


#This is a program for simple interest
P=float(input("Enter the value of p :"))
r=float(input("Enter the value of r:"))
t=float(input("Enter the value of t:"))
Simple_interest=(P*r*t)/100
print("This is the S.I=",Simple_interest)


#This program is of a simple calculator 
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
print("SUM:",a+b,"\nSUBSTRACTION:",a-b,"\nProduct:",a*b,"\nDivision:",a/b)

#THIS IS A PROGRAM TO DO SUM AND FIND LENGTH OF A STRING
a=[13,45,67,23]
print(len(a))
print(sum(a))

#This is a program to acces string character using index
n=("apple","mango","banana","orange")
print(n[2])

#this is a program to find lenght access character using index and do upper and lower casing
a="compilers are used to execute program all at once and shows the errors after compilation"
print(len(a))
print(a[8])
print(a.upper())
print(a.lower())

#This is a program use to concatinate(add) two strings
a=("Hi Everyone")
b=(" how are you")
print(a+b)
