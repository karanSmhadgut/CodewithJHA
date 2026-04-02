p_amount = int(input("enter principal amount :"))
roi = int(input("enter rate of interes :"))
time = int(input("duration of loan :"))

si = p_amount*roi*time/100
print("*simple interset=",si)