#question1
x=int(input("insert first number:"))
y=int(input("insert second number:"))
z=int(input("insert third number:"))
average=(x+y+z)/3 #formula for taking average of 3 given numbers
print("Average of three no.s:",average)

#question2
grossamt=int(input("gross amount=$"))
sd=10000  #sd stands for standard deduction
print("standard deduction=$",sd)
dd=3000   #dd stands for dependent deduction
print("dependant deduction=$",dd)
dependents=int(input("no.of dependents(if any):"))
taxrate=0.20
print("taxrate=20%")
taxableamount=grossamt-sd-(dd*dependents)
print("taxable amount is=",taxableamount)
tax=taxableamount*taxrate
print("tax=",tax) #to print a person's income tax

#question3
sid=int(input("Enter your SID:"))
name=str(input("Enter your name:"))
gender=input("gender(use F for female,M for male,U for unknown):")
course=str(input("Enter course name:"))
cgpa=float(input("Enter your CGPA:"))
x=[sid,name,gender,course,cgpa] #list for student information
print("STUDENT INFORMATION:",(x))

#question4
p=float(input("enter student 1 marks:"))
q=float(input("enter student 2 marks:"))
r=float(input("enter student 3 marks:"))
s=float(input("enter student 4 marks:"))
t=float(input("enter student 5 marks:"))
total=[p,q,r,s,t]  #here p,q,r,s,t represent marks of students 1-5 respectively
print("Marks of all students",total)
total.sort() #to sort the list in increasing order
print("Sorted list of marks:",total)

#question5
colors=["red","green","white","black","pink","yellow"]
print("original list",colors) #this is the original lest
print("Question 5(a)")
del colors[3]  #3 is the index of colour black which is to be deleted
print("new list",colors)

print("Question 5(b)")
color=["red","green","white","black","pink","yellow"]
color[3:5]=["purple"] #to remove colors with index 3,4 and add color purple
print("final list",color)

      
