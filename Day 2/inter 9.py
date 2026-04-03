# list1=['prashant','jha']
# # print(list1*2)
# list2=[50,25.50,'prashant']
# print(list1+list2)
# del list2
# del list2[2]
# print(list2)

# list2 = [50, 25.50, 'prashant']  
# list2.clear()  
# print(list2)

name = "prashant"  
print(name)  
myname = list(name)  
print(myname)

# mylist = [40, 30, 20, 10]  
# mylist.reverse()  
# print(mylist)


mylist = [44, 22, 77, 0, 9, 88]  
mylist.sort(reverse=True)  
print(mylist)

# default  sorting order is ascending
# default sorting order is string is alphabetic

mylist = [44, 22, 77, 0, 9, 88]  
newlist = mylist  
print(id(mylist))   
print(id(newlist))