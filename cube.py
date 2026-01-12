#input: number
#output: cube number
#problem: make a  number to its cube
#solution: 

def cub_number(n):
    return n*n*n
# print(cub_number(7))

# for i in range(1,11):
#     print(f"Cube number of {i}  is " ,cub_number(i))

i=1
while i<=10:
    print(f"Cube of {i} is ", cub_number(i))
    i+=1
    