#ques 1
inputstring="Python is a case sensitive language"
#a
print("Length of string is=",len(inputstring))
#b
print("Reverse of string is:",inputstring[::-1])
#c
newstring=inputstring[10:26]
print(newstring) #saved a case sensitive in new string
#d
print(inputstring.replace("a case sensitive","object oriented"))
#e
print("index of 'a':",inputstring.index("a"))
#f
print("String without space:",inputstring.replace(" ",""))


#ques2
name="Daanisha Singla"
sid="21104040"
department="Electrical"
cgpa="9.9"
#personal details stored in different variables
print("Hey,",name,"Here!",'\n' "My SID is",sid,'\n' "I am from",department,"and my cgpa is",cgpa)

#ques3
a=56
b=10
#using bitwise operators
print("a&b",a & b)
print("a|b",a | b)
print("a^b",a ^ b)
print("a<<2:",a<<2,"b<<2:",b<<2) #left shift both a and b with 2 bits
print("a>>2:",a>>2,"b>>2:",b>>2) #right shift both a and b with 2 bits

#que4
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
c=float(input("Enter the third number:"))
#commands to find largest number of given 3
if(a>=b and a>=c):
    print("The largest number among these three is",a)
elif(b>=a and b>=c):
    print("The largest number among these three is",b)
else:
    print("The largest number among these three is",c)

#ques5
inputstr=input("Enter input string:")
if "name" in inputstr:    #to check whether 'name' is present in string or not
    print("YES")
else:
    print("NO")

#ques6
a=int(input("Enter the first side:"))
b=int(input("Enter the second side:"))
c=int(input("Enter the third side:"))
#commands to check if triangle will be formed or not
if b+c>a:
    print("Yes,triangle will be formed")
elif a+c>b:
    print("Yes,triangle will be formed")
elif  a+b>c:
    print("Yes,triangle will be formed")    
else:
    print("No triangle will be formed")






