#Introduction to Python
    #Guido Van Rossum and released in 1991
    #Used for Web dev(Serverside), Software dev, Mathematics, System scripting
    #Instaled python on computer
    #Installed google collab on my gDrive

#Python variables
#Variable is a name that is used to refer to memory location. Python variable is also known as an identifier and used to hold value.
print("John is male")
print(type("Jene"))
#Write a program for a hospital 

 #   Check in a patient named John Smith
 #   He is 20 years old
    #  He is a new Patient
#Declare variables to store this values
patientName = "John Smith"
Age = 20
newPatient = True
print(patientName + " is " + str(Age) + " years and he is a new patient")

#Datatypes and Keywords
#integer, float, string, List, Tuple, and dictionary
#Python is a dynamically typed language; hence we do not need to define the type of the variable while declaring it.
# The interpreter implicitly binds the value with its type.
Male = True
s = type(Male)
print(Male)
print(s)
#Python Keywords are not to be used by variables


#List  and Tuple
List1 = ['JavaTpoint', 1, 2, 54.30, {'Name: ''Peter'}]#Mutabble
print(type(List1))
tuple2 = ('JavaTpoint', 1, 2, 54.30, {'Name: ''Peter'}, [1,2,3])#Immutable
print(type(tuple2))
print(List1)
print(tuple2)
print(len(tuple2) - len(List1))
set1 = {12,34,'f',55}#uses least possible speed
print(set1)
print(List1[3])
print(tuple2[1])
print(tuple2[0])

#Operators
#Operators are the pillars of a program
#  on which the logic is built in a specific programming language.
   # Arithmetic operators
num1, num2, num3, num4, num5 = 9, 18, 55, 85, 90.4
x = num5 + num3
print(x)

y = num3 - num2
print(y)

z = num5 / num1
print(round(z,5))

v = num2 * num1
print(v)

b = num4 % num1
print(b)

a = num4 // num1
print(a)
c = num5 // num1
print(c)

d = num3 ** num1
print(d)
w = pow(num3,num1)
print(w)

   # Comparison operators
print(num5 > num3)
print(num1 < num2)
print(num3 == num4)
print(num4 != num1)
print(num5 <= num2)
print(num5 >= num2)



   # Assignment Operators
j = 5
k = "Beni"
l = "Christine"
j1 = 2
print(j1)
j1 += 3 # j1 = j1 + 3
print(j1, j,'\n', k, l)
j *= 5
j1 -= 2 #j1 = j1 -2
print(j1,'\n', j)
print(5|2)

   # Logical Operators
# and , or, not
g = num3 < num4 and num2 > num1
print(g)
print(not(g))
h = num3 < num4 or num2 < num1
print(h)
print(not(h))


   # Bitwise Operators
# & AND, | OR, # ^ XOR, ~ NOT,<< Zero fill left shift, >> Signed right shift

   
   # Membership Operators
# in, not in
if 5 in List1:
    print("Found")
elif 5 not in List1:
    print("Not found")
else:
    print("Search error")


    #Identity Operators
#is and is not
#Identity operators are used to compare the objects,
# not if they are equal, but if they are actually the same object,
# with the same memory location:
print(a is b)



#User input in Python
userName = input("Enter Name: ")
print("Hello " + userName)
print("Happy Birthday " + userName[5:] + " !!")

#Bitwise Operators

#Selftestexercises
#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask the user for their salary and year of service and print the net bonus amount.
# Write a python code to implement this scenario.
employeeName = input("Enter Name: ")
yearOfService = int(input("How long have you worked here?(years): "))
salary = float(input("Earnings per Month: "))
bonusPercentage = 0.05

def salaryRaise():
    if yearOfService > 5:
        bonusAmount = bonusPercentage * salary
        print("Thank you ", employeeName,".\n" , "Your salary raise is " + str(salary + bonusAmount), ".")
    else:
        print("After ", 5 - yearOfService, " years, You will receive your bonus.")

salaryRaise()



#Questions in intro t Pyton

