# # arr = [[1,2,3,4],
# #        [4,5,6,7],
# #        [8,9,10,11],
# #        [11,12,13,14]]
# # for i in range (0,4):
# #     print(arr[i].pop())
# #     4 7 11 14

# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1] = arr[i]
# for i in range(0,6):
#     print(arr[i], end = " ")  
    #2 3 4 5 6 6
    
fruit_list1 =['apple','berry','cherry','papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
fruit_list2[0] = 'guava'
fruit_list3[1] = 'kiwi'

sum= 0
for Is in (fruit_list1,fruit_list2,fruit_list3):
 if Is[0] == 'guava':
        sum += 1
if Is[1] =='kiwi':
    sum+=20
print(sum)
        