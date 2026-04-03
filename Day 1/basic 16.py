#Write a program to accept physics, chemistry and maths. Subject marks.
# Calculate total percentage and if percentage is greater than equal to 60 is equal to male, 
# so he’s eligible for placement eligible for data job.

physics= int(input("marks of physics:"))
chemistry= int(input("marks of chemistry:"))
maths= int(input("marks of maths:"))
gender = input("enter your gender")
total =physics+chemistry+maths

percentage = total/3.0
print("total:",total)
print("precentage:",percentage)

if percentage>60 and gender =="male":
    print(" student is eligible placement ")
else :
    print ("eligible for data entry")