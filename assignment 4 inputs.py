#question 1
print("Ques 1")
#Creating a recursive function  
def tower_of_hanoi(disks, source, auxiliary, target):  
    if(disks == 1):  
        print('Move disk 1 from rod {} to rod {}.'.format(source, target))  
        return  
    # function call itself  
    tower_of_hanoi(disks - 1, source, target, auxiliary)  
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))  
    tower_of_hanoi(disks - 1, auxiliary, source, target)  
  
disks=3
# We are referring source as A, auxiliary as B, and target as C  
tower_of_hanoi(disks, 'A', 'B', 'C')  # Calling the function

#question2
print("Ques 2")
r = int(input("Enter the number of rows in Pascal's Triangle: "))

#using loops
print("Using loops: ")
for rows in range(1,r+1):
    print('  '*(r - rows),end=' ')#to print space according to the number of rows entered
    count = 1 #Pascal's triangle will start with 1 
    for i in range(1, rows+1):
        print(count,end='  ') 

        count = count*(rows - i) // i #// rounds the division into nearest whole number
    print()

#using recursions
print("Using recursions: ")
def PascalTriangle(r,checkr=r):
    if (r==0):
        return
    
    PascalTriangle(r-1,checkr)
    print('  '*(checkr-r),end=' ')
    count2 = 1 
    for i in range(1, r+1):
        print(count2,end='  ')
        count2 = count2*(r - i) // i
    print()
PascalTriangle(r)

#question 3
print("Ques 3")
#taking inout from user
a=int (input('Enter first number: '))
b=int (input('Enter second number: ')) 
o=divmod (a, b)
print("(quotient, remainder:)",o) #finding quotient and remainder
#sub parts using built-in functions 
print('(a)')
print('is function callable?: ',callable(o))
print('(b)')
print('are all values non zero?:',all(v!=0 for v in o))
print('(c)')
t=o+(4,5,6)
print("output with added values:",t)
t=tuple(filter(lambda x:x<=4, t))
print('output with filtered values: ',t)
print('(d)')
s=set (t)
print('set: ',s)
print('(e)')
f=frozenset(s)
print('immutable set: ',f)
print('(f)')
m=max(s)
print('maximum value in set: ',m)
print('hash of max value:',hash (m))

#question 4
print("Ques 4")
#creating class
class Student:
    def __init__(self,name,rollno):
        print("Student data created!")
        self.name=name
        self.rollno=rollno
    def __del__(self):
        print("Student data destroyed!")
#creating objects in class
s1Name=str(input("Enter name of student 1: "))
s1Rollno=int(input("Enter roll no of student 1: "))
S1=Student(s1Name,s1Rollno)
s2Name=str(input("Enter name of student 2: "))
s2Rollno=int(input("Enter roll no of student 2: "))
S2=Student(s2Name,s2Rollno)
s3Name=str(input("Enter name of student 3: "))
s3Rollno=int(input("Enter roll no of student 3: "))
S3=Student(s3Name,s3Rollno)
#calling __del__() function to destroy object
print("Deleting data of student 3: ")
del S3

#question 5
print("Ques 5")
#creating class to store employee's data
class Employees:
    def __init__(self,name,salary):
        print("Employee data added")
        self.name=name
        self.salary=salary
    def __del__(self):
        print("Employee data destroyed")
    def update(self,salary):
        self.salary=salary
        print("Salary updated for Mehak")
#adding employees
E1=Employees('Mehak',40000)
E2=Employees('Ashok',50000)
E3=Employees('Viren',60000)
print("(a)")
#updating Mehak's salary
Employees.update(E1,70000)
print("(b)")
#deleting Viren's record
del E3

#question 6
print("Ques 6")
gap=" "*10
print(f"\n{gap}THE FRIENDSHIP GAME")
#definig principle of game i.e. anagram
def anagram(word1,word2):
    #converting all letters to lowercase
    word1=word1.lower()
    word2=word2.lower()
    #form empty list to store letters 
    l1=[]
    l2=[]
    for e in word1:
        l1.append(e)
    for el in word2:
        l2.append(el)
    #sorting the list alphabetically
    l1.sort()
    l2.sort()
    if l1==l2:
        return True
    else:
        return False

#taking words spoken by written
word_player1=str(input(f"\nEnter Word by GEORGE:"))
word_player2=str(input(f"Enter Word by BARBIE:"))
#using anagram function
result=anagram(word_player1,word_player2)
#printing the final result
if result==True:
    print(f"\nFriendship of GEORGE and BARBIE is REAL")
elif result==False:
    print(f"\nFriendship of GEORGE and BARBIE is FAKE")




