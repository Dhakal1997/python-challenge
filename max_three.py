#input:
#output:
#problem:
#solution:
def find_max(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >=a and b >= c:
        return b
    else:
        return c
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
print(find_max(x,y,z))
