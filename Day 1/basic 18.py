# # # day=input("enter a day name :")

# # # if day=="saturday" or day=="SATURDAY" or day=="sunday" or day=="SUNDAY" :
# # #     print("IS weekend")
# # # else :
# # #     print("working day")
    
    


# # msg = input("Enter a msg: ")

# # if 'A' <= msg <= 'Z':
# #     print("Uppercase alphabet")
# # elif 'a' <= msg<= 'z':
# #     print("Lowercase alphabet")
# # else:
# #     print("Special character")
# #     #
# a=ord(input("Enter any key"))

# if a>=65 and a<=91:
#     print("Uppercase")
# elif a>=97 and a<=122:
#     print("Lowercase")    
# elif a>=48 and a<=57:
#     print("Digit")
# else:
#     print("special character")
    
#WAP to change calculation with respect to total amount.
amount = int(input("Enter the total amount: "))
print("100 notes =", amount//100)
print("50 notes =", (amount%100)//50)
print("20 notes =", ((amount%100)%50)//20)
print("10 notes =", (((amount%100)%50)%20)//10)
print("5 notes =", ((((amount%100)%50)%20)%10)//5)