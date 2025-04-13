# n = int(input())
def check_weired(n):
    if (n % 2 != 0) or (n in range(6,21,2)):
        return "Weird"
    else:
        return "Not Weird"
        
        
i=1
while i<=30:
    print(f"{i} is : ?",check_weired(i))
    i+=1