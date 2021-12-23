
def Minimum(num1, num2):
    if num1<num2:
        return num1
    return num2

print("Program calculates the minimum number\n")
num1=int(input("Input first number: "))
num2=int(input("Input first number: "))
print("Minimal number of the pair:",Minimum(num1,num2))