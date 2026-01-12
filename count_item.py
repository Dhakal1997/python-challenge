#input: []
#output: total time of occurence
#problem: total time of occurence
#solution: 
#step 1st: itterate to every item
#second step: count methods in list



def count_item(list):
    # Empty initially to hold unique value that not exists in the list.
    unique = []
    # for iterration to every element
    for item in list:
        #track_item = list.count(item)
        
        if item not in unique:
            #To append new object thats not in the list already
            unique.append(item)
    # for iteration to every item in unique list        
    for element in unique:
        print(f"{element} Count is ", list.count(element))
        
       # print(f"{item} Count is ",track_item)
# Make a list of each item with occurence       
given_list = [1,2,3,2,5,3,2,5,3,3,3,1,4]    


count_item(given_list)   


        
        
        
       



