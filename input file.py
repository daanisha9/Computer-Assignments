#question 1
from tkinter import*
#defining function to find GST
def gst_finder() :
    ogc=int(ogcField.get())
    ntp=int(ntpField.get())
    gst=((ntp-ogc)*100/ogc)
    gstFinder.insert(10,str(gst)+'%')
def clear():
    ogcField.delete(0,END)
    ntpField.delete(0,END)
    gstFinder.delete(0,END)
#creating GUI
win=Tk()
win.title('question 1')
win.geometry('400x400')
lb1=Label(win,text='enter original cost: ',bg='black',fg='white',font=('Arial'))
lb1.place(x=10,y=20)
lb2=Label(win,text='enter net price: ',bg='black',fg='white',font=('Arial'))
lb2.place(x=10,y=60)
find = Button(win, text = "Find", fg = "Black",bg = "yellow",command = gst_finder)
find.place(x=200,y=100)
lb3=Label(win,text='GST rate is: ',bg='black',fg='white',font=('Arial'))
lb3.place(x=10,y=140)
clear = Button(win, text = "Clear", fg = "Black",bg = "yellow",command = clear)
clear.place(x=200,y=180)
ogcField=Entry(win)
ogcField.place(x=200,y=20)
ntpField=Entry(win)
ntpField.place(x=200,y=60)
gstFinder=Entry(win)
gstFinder.place(x=200,y=140)
win.mainloop()

#question 2
from tkinter import*
#importing calender
import calendar
#to print calendar for a given year
def ShowCal():
    new=Tk()
    new.title('Calendar')
    new.geometry('550x600')
    fetch=int(year.get())
    content=calendar.calendar(fetch)
    cal_year=Label(new,text= content, font='Consolas 10')
    cal_year.grid(row = 5, column = 1, padx = 20)
    new.mainloop()
#creating GUI
main=Tk()
main.title('question 2')
main.geometry('400x400')
cal=Label(main,text='CALENDAR',font=('Arial',20,'bold'))
lb=Label(main,text='Enter Year: ',bg='White',fg='Black')
lb.place(x=20,y=40)
year=Entry(main)
year.place(x=100,y=40)
Show = Button(main, text = "Show Calendar", fg = "Black", command = ShowCal)
Show.place(x=100,y=80)
Exit = Button(main, text = "Exit", fg = "Black", command = exit) #details for window
Exit.place(x=100,y=120)
main.mainloop()

#question 3
from tkinter import*
win=Tk()
win.title('question 3')
#defining various functions to carry out calculations
def click(item):
    global expression
    expression=expression+str(item)
    input_num.set(expression)
def btn_clear():
    global expression
    expression=''
    input_num.set('')
def btn_equal():
    global expression
    result=str(eval(expression))
    input_num.set(result)
    expression=''
expression=''
input_num=StringVar()
input_field=Entry(textvariable=input_num,justify=RIGHT)
input_field.grid(row=0,column=1)
#first row
clear=Button(text='Clear',bg='White',fg='Black',command=lambda:btn_clear())
clear.grid(row=0,column=0)
divide=Button(text='/',bg='White',fg='Black',command=lambda:click('/'))
divide.grid(row=0,column=2)
#second row
seven=Button(text='7',bg='White',fg='Black',command=lambda:click('7'))
seven.grid(row=1,column=0)
eight=Button(text='8',bg='White',fg='Black',command=lambda:click('8'))
eight.grid(row=1,column=1)
nine=Button(text='9',fg='Black',bg='White',command=lambda:click('9'))
nine.grid(row=1,column=2)
multiply=Button(text='*',fg='Black',bg='White',command=lambda:click('*'))
multiply.grid(row=1,column=3)
#third row
four=Button(text='4',fg='Black',bg='White',command=lambda:click('4'))
four.grid(row=2,column=0)
five=Button(text='5',fg='Black',bg='White',command=lambda:click('5'))
five.grid(row=2,column=1)
six=Button(text='6',fg='Black',bg='White',command=lambda:click('6'))
six.grid(row=2,column=2)
minus=Button(text='-',fg='Black',bg='White',command=lambda:click('-'))
minus.grid(row=2,column=3)
#fourth row
one=Button(text='1',fg='Black',bg='White',command=lambda:click('1'))
one.grid(row=3,column=0)
two=Button(text='2',fg='Black',bg='White',command=lambda:click('2'))
two.grid(row=3,column=1)
three=Button(text='3',fg='Black',bg='White',command=lambda:click('3'))
three.grid(row=3,column=2)
plus=Button(text='+',fg='Black',bg='White',command=lambda:click('+'))
plus.grid(row=3,column=3)
#fifth row
zero=Button(text='0',fg='Black',bg='White',command=lambda:click('0'))
zero.grid(row=4,column=0)
point=Button(text='.',fg='Black',bg='White',command=lambda:click('.'))
point.grid(row=4,column=2)
equal=Button(text='=',fg='Black',bg='White',command=lambda:btn_equal())
equal.grid(row=4,column=3)

win.mainloop()

#question 4
input_string=input('Enter marks of students separated by space: ')
userlist=input_string.split()
print('List of unsorted marks: ',userlist)
#defining a function that will take last element as pivot
#correct position in array, and then places all smaller(smaller than pivot) to
#lest of pivot and greater ones to right of pivot.
def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            (arr[i],arr[j])=(arr[j],arr[i])
    (arr[i+1],arr[high])=(arr[high],arr[i+1])
    return i+1
#defining main QuickSort function
def quickSort(arr,low,high):
    if len(arr)==1:
        return arr
    if low<high:
        pi=partition(arr,low,high)#pi is partition index
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
#QuickSort function
arr=userlist
n=len(userlist)
quickSort(arr,0,n-1)
print('list of marks(sorted): ',arr)

#question 5
#taking input from user and making a list
user_list=list(map(int,input('enter elements of array seperated by space: ').strip().split()))
print('input array: ',user_list)
print('\n(a)')
#sorting the list
user_list.sort()
print('sorted list: ',user_list)
print('\n(b)')
#defining Binary Search function
def BinarySearch(arr,low,high,x):
    if high>=low:
        mid=(high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return BinarySearch(arr,low,mid-1,x)
        else:
            return BinarySearch(arr,mid+1,high,x)
    else:
        return -1
arr=user_list
x=int(input('enter element to be searched: '))
#calling the function
result=BinarySearch(arr,0,len(arr)-1,x)
if result!= -1:
    #if elemnt present in user entered array
    print('element is present at index, ',str(result))
    print('\n(c)')
    print('the number of occurences of element is: ',user_list.count(x))
else:
    #if element not present
    print('ERROR! element is not present.')







