# first programm - class example
class Student:
    def check_pass_fail(self):
        if self.mark>=40:
            return True
        else:
            return False
student1=Student()
student1.name="Harry"
student1.mark=80
did_pass = student1.check_pass_fail()
print(did_pass)

student2=Student()
student2.name="Janet"
student2.mark=34
did_pass= student2.check_pass_fail()
print(did_pass)
# second programm - init func
class Student2():
    def check_pass_fail2(self):
        if self.marks>=40:
            return True
        else:
            return False

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

student3=Student2("Garry",78)
student4=Student2("Anna",23)
did_pass2=student3.check_pass_fail2()
print(did_pass2)
did_pass2=student4.check_pass_fail2()
print(did_pass2)

# third programm - complex numbers
class Complex():
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def add(self,number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = Complex(real,imag)
        return result
n1=Complex(4,5)
n2=Complex(-6,2)
result=n1.add(n2)
print("Real part of number:",result.real)
print("Imag part of number:",result.imag)  

