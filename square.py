#input: number
#output: square number
#problem:finding square number in  range
#solution: Dividing into small parts
#part 1st: function to square a number
#part 2nd:

def sq_number(n):
    return n*n
print(sq_number(5))

for n in range(1,11):
    print(f" Square of {n} is",sq_number(n))
    






