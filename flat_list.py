input = [3, 6,[1,2,3],[4,5,6,[1,3]], 22]
#output = [3,6,1,2,3,4,5,6,22]

def flat_list(arr):
    result = []
    for item in arr:
        if (type(item) == list):
            result.extend(flat_list(item))
        else:
            result.append(item)    
        
    return result
    

print(flat_list(input))
# print((type(3) == list))
# print("Neew copy",isinstance({1:"hey"}, dict))
# print(result)


# a =5
# a =6
# a=9
# print("final value is", a)