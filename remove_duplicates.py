#input:[1,2,6,3,2,6,8,10,8,6,7,9,4,5]
#output:[1,2,3,4,5,6,7,8,9,10]
#problem:removine duplicates items in listof numbers
#solution: for loop to iterrate the list.use memebership

list = [1,2,6,3,2,6,8,10,8,6,7,9,4,5]
# new_list = []
# for item in list:
#     if item not in new_list:
#         new_list.append(item)
#         print(new_list)
 
def remove_duplicate(list):
    new_list = []  
    for item in list:
        if item not in new_list:
            new_list.append(item)
    return(new_list) 
print(remove_duplicate(list))



            
            
        
        
        
    