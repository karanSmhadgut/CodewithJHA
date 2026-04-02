#nested if else:#WAP to accept value of A,B,c and find the Max value

a = int(input("enter  value for a :"))
b = int(input("enter  value for b :"))
c = int(input("enter  value for c :"))

if a>b :
    if a>c:
     print("a is greater")
    else:
     print("c is greater ")
else:
    if b>c:
     print("b is greater")
    else:
     print("c is greater")
     