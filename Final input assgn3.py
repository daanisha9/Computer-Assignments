#ques1
string_name=str(input("Enter the string:")) #input
#Taking each string as element in list
list1=string_name.split()
list_l=[]
for e in list1:
    list_l.append(e)
#converting list_l to set to avoid repeatation
set1=set(list_l)
dic={}
#dictionary with key string and value string count
for el in set1:
    count=list_l.count(el)
    dic.update({el:count})
#Code when string contains only one word
dic2={}       
set2={1,2}
set2.clear()  
list2=[]      
#Condition when only one word is detected in string
if len(list1)==1:
    #Code for counting letter
    for elements in string_name:
        list2.append(elements)
    for el in list2:
        set2.add(el)
    for elem in set2:
        #Adding count values to dic2
        dic2.update({elem:string_name.count(elem)})
    # printing the dic2 containing 'letter':'letter count'
    print("\nDictionary containing the 'Count' is shown below:")
    print(dic2)
#printing the dic when string contains more than one word
else:
    print("\nDictionary containing the 'Count' is shown below:")
    print(dic)      #dic contains 'word':'word count'


#ques2
print("Enter Date below to get date of next day.\n")
def leapyear(x):
    
    if(x%4==0):
        return True
    else:
        return False
#Taking input day,month,year
day=int(input("Enter date:"))
month=int(input("Enter month:"))
year=int(input("Enter year:"))
print(f"\nPresent Date:",day,"/",month,"/",year)
#Applying condition1 for dates out of range
if 1<day<31 or 1<month<12 or 1800<year<2025:
    condition1=True
else:
    condition1=False


month_31 = [1,3,5,7,8,10,12]  
month_30 = [4,6,9,11]   

c1a= day==31 and (month in month_30)

c1b= day>29  and month==2

c1c= day==29 and (not leapyear(year)) and month==2
if c1a or c1b or c1c :
    condition2=False
else:
    condition2=True
#printing error when date entered is not correct
if c1a:
    print(f"\nError\n{day} day can't be in month {month}")
elif c1b:
    print(f"\nError\n{day} day can't be in month {month}")
elif c1c:
    print(f"\nError\n{day} day can't be in month {month} as the year {year} is not a leapyear")
elif condition1==False:
    print(f"\nError\nPlease enter date in range day[1-31], month[1-12], year[1800-2025] ")


if condition1==True and condition2==True :
    month_31 = [1,3,5,7,8,10,12]  
    month_30 = [4,6,9,11]   
    #For month with 31 days
    if (month in month_31) == True:
        if day == 31 and month==12:
            day = 1
            month = 1
            year=year+1
        elif day==31 and month!=12:
             day=1
             month=month+1
        elif 1 <= day <= 30:
            day = day + 1
    #For month with 30 days
    elif (month in month_30) == True:
        if day == 30:
            day = 1
            month = month+1
        elif 1 <=day<=29:
            day = day + 1
    #for february month i.e. month 2
    elif month == 2:
        # If year is leap year
        if leapyear(year) == True:
            if day == 29:
                day = 1
                month = month + 1
            elif 1 <= day <= 28:
                day = day + 1
        # If year is not leap year
        elif leapyear(year) == False:
            if day == 28:
                day = 1
                month = month + 1
            elif 1 <= day <= 27:
                day = day + 1
    # Printing Next date
    print(f"\nNext Date is:{day}/{month}/{year}")


#ques3
#Taking input list
list1=list(map(int,input("Enter the numbers:").split())) #numbers written with a space
list2=[]
#storing in tuple
for n in list1:
    tuple=(n,n**2)
    list2.append(tuple)
#final result
print("\nList containing (n,n^2) is shown below:")
print(list2)

#ques4
gradept=int(input("Enter your grade points:")) #taking input from user
dic={10:"Your grade is 'A+' and Outstanding performance.",
     9:"Your grade is 'A' and Excellent performance.",
     8:"Your grade is 'B+' and Very Good performance.",
     7:"Your grade is 'B' and Good performance.",
     6:"Your grade is 'C+' and Average performance.",
     5:"Your grade is 'C' and Below Average performance.",
     4:"Your grade is 'D' and Poor performance."}   #each grade point has its specific remark
if 4<=gradept<=10:
    statement=dic.get(gradept)
    print(statement)
else:
    print("Enter valid grade points!")
    
#ques5
print("The pattern is printed below:\n")
abcd = "ABCDEFGHIJK"
# forming a list of letters
list_abcd = []
for i in abcd:
    list_abcd.append(i)
# Applying while loop to print only required rows
k = 1
while k <= 6:
    # printing 1st row intially when k=1
    for el in list_abcd:
        print(el, end="")
    # forming second row elements to be printed
    list_abcd.pop(len(list_abcd) - 1)  
    list_abcd.pop(len(list_abcd) - 1)  # removing last 2 element of list
    list_abcd.insert(0, " ")  # insertind space
    print() 
    k = k + 1


#ques6
#By default 1st run
repeat="Y"
#Intially empty dictionary
dic={}
dic2={}
#List containing Y or N
liste=["Y","N"]
#Main code
while repeat=="Y":
    #Taking input name and sid
    name = str(input("Enter student name:"))
    sid = int(input("Enter student SID:"))
    if sid<0:
        print("\nError\nSID can't be negative\n")
    else:
        # Updating dic with 'sid':'name'
        dic.update({sid: name})
        # updating dic 2 with 'name':'sid'
        dic2.update({name:sid})
        #to enter more input or not
        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break
    elif (not (repeat in liste)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end:"))

# a
#printing the dictionary
print("\nQ.6(a)")
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)
# b
#sorting according to name
print("\nQ.6(b)")
list_k=sorted(dic2)
dic3={}
for ele in list_k:
    dic3.update({dic2.get(ele):ele})
print("The Dictionary after sorting according to name:")
print(dic3)

# c
#sorting according to SID
print("\nQ.6(c)")
sort_dic = sorted(dic)
dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID:")
print(dic4)
# d
print("\nQ.6(d)")
# Taking input SID to be searched
entersid = int(input("Enter SID to get name of student:"))
# Searching for sid as key in dic
outputname = str(dic.get(entersid))
print(f"Name of student with SID {entersid} is {outputname}.")

#ques7    
#Taking input
n=int(input("Enter number of elements N in fibonacci series:\n[N must be positive Integer]: N="))
if n<=0 :
    print("\nError\nNumber of elements in fibonacci series must be an integer and greater than zero.")
#code for fibonacci series
else:
    #code for fibonacci series for first 2 elements
    if n == 1:
        print("\nThe fibonacci series with 1 element is shown below\n[1]")
        print("\nAverage of given fibonacci series is", 1)

    elif n == 2:
        print("\nThe fibonacci series with 2 element is shown below\n[1,1]")
        print("\nAverage of given fibonacci series is", 1)
    #General code for fibonacci for next N-2 elements
    else:
        # List of fibonacci elements with 1,1 as initial elements
        list1 = [1, 1]
        a = 1
        b = 1
        # For loop
        for i in range(n - 2):
            s = a + b
            list1.append(s)
            a = b
            b = s
        # printing the final fibonacci series
        print(f"\nThe fibonacci series with {n} elements is shown below:")
        print(list1)
        # Finding average of fibonacci series
        sum = 0    #intial sum=0
        # finding sum of all elements in list1
        for num in list1:
            sum = sum + num
        average = (sum / n)
        # Till two decimal place
        twodecimal = "{:.2f}".format(average)
        # printing average
        print(f"\nAverage of given fibonacci series is {twodecimal}")

#ques8
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}
#printing the given sets
print(f"Set1= {set1}\nSet2= {set2}\nSet3= {set3}")
#a
print("\nQ.8(a)")
print("\nA new Set of all 'elements that are in Set1 and Set2 but not both' is:",set1^set2)
#b
print("\nQ.8(b)")
print("\nSet of elements that are in only one of the three sets:",set1^set2^set3)
#c
print("\nQ.8(c)")
print("\nA new set of elements that are 'exactly in two of the sets Set1, Set2 and Set3' is:",set1&set2|set2&set3|set1&set3)
#d
print("\nQ.8(d)")
print("\nA new set of all Integers in the 'range 1 to 10' that are 'not in Set1' is:",set(range(1,10))-set1)
#e
print("\nQ.8(e)")
print("\nA new set of all Integers in the range 1 to 10 that are not in Set1,Set2 and Set3.",set(range(1,10))-set1-set2-set3)


        
        
    
    

    
    




    

