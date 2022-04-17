# solved in 4m
size = int(input())

def triangle(a):
    for i in range(a+1):
        print((size-i)*" "+(1+2*i)*"*")


for i in range(size):
    triangle(i+1)

print(" "*size+"|")
print("="*size+"V"+"="*size)
