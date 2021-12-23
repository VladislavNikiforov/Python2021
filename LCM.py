def LCM(a,b):
    an,bn=a,b
    while True:
        if a>b:
            b+=bn
        elif a<b:
            a+=an
        else:
            return a
a=int(input("input two numbers, program defines LCM"))
b=int(input())
print(LCM(a,b))
