
def MinArg(*args):
    k=99999999999999999 #очень большое число
    for i in args:
        if i<k:
            k=i
    return k
lst=[]

n=int(input("How many numbers you want to sum"))
for i in range(0,n):
    ele=input("Input number: \n")  
    lst.append(ele)
print("Minimal from the tuple: ",MinArg(lst))
