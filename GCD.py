def GCD(a,b):
    while True:
        if a==0 or b==0:
            break
        if a>b:
            a%=b
        elif a<b:
            b%=a
    return a+b
a=int(input())
b=int(input())
print("answer is",GCD(a,b))
