# 1 km = 0.621371 miles
kmToMile = 0.621371
distance = 564.5
distance_miles = distance * kmToMile
print(distance_miles)
# second programm

number = int(input("Enter a number: "))
count=10
while count>0:
    print(count*number)
    count-=1

# third programm
# outputs 1,2,3,4,5
result=0
for cnt in range(1,101):
    result+=cnt
print(result,"\n")
# fourth programm
languages = ["Python", "Java", "Swift", "C", "C++"]
for language in languages:
    if language == "Swift" or language == "C++":
        continue
    print(language)
# fifth programm
num5=5.0
if num5>0.0:
    pass
print("\n")
# do nothing - empty body

# sixth programm
import statistics

def compute_average(marks):
    grade=''
    average_mark=statistics.mean(marks)
    if average_mark>=80:
        grade='A'
    elif average_mark>=60 and average_mark<80:
        pgrade='B'
    elif average_mark>=50 and average_mark<60:
        grade='C'
    elif average_mark<50:
        grade='F'
    else:
        grade='e'
    return grade

marks=[55,64,75,80,65]
print(compute_average(marks))
# seventh programm - funcs
def add_number(*args):
    sum=0
    for num7 in args:
        sum+=int(num7)
    return sum

def multiple_number(*args):
    mult=1
    for num8 in args:
        mult*=int(num8)
    return mult
a,b = 5,6
print("Sum of numbers:", add_number(a,b))
print("Mult of numbers:", multiple_number(a,b))

# eigth programm - strings
quote="Talk is cheap. Show me the code."
print("1.",quote[3])
print("2.",quote[-3])
print("3.",quote.replace("code","programm"))
# ninth programm - dictionaries
synonims={"mountain":"peak", "forest":"jungle"}
print("1.", synonims["mountain"])
synonims["terrain"]="land"
print("2.",synonims)
synonims.pop("forest")
print("3.",synonims)
# tenth programm
animals = {"dog", "cat", "tiger","elepgant", "dog"}
print("1.",animals)
animals.remove("cat")
animals.discard("dog")
print("2.",animals)
animals.add("snake")
print("3.",animals)
result = {1,5,10,23} & {1, 100, 3, 5}
print("4.",result)
animals1 = {"cat","dog"} | {"cat", "dog", "snake"}
print("5.",animals1)
# eleventh task
result=list(range(3,33,3))
print(result)