#factorial of a number 
# n=int(input("enter a number"))
# f=1
# #if n%i==1:
# for i in range(1,n+1):
#  #print('i:', i)
#   f=f*i
# print('f:', f)

#find largest among three numbers

# n1=10
# n2=50
# n3=20

# if n1>=n2 and n1>=n3:
#   print("n1:",n1)
# elif n2>=n1 and n2>=n3:
#   print("n2:",n2)
# else:
#   print('n3:',n3)

#sorting without sort method(Ascending order)

# a=[]
# n1=int(input("enter the number: "))
# for i in range(n1):
#     n2=int(input("enter %d item number: " %i))
#     a.append(n2)
# for i in range(n1-1):
#     for j in range(n1-1-i):
        
#         if(a[j] > a[j+1]):
#             print("1st staement a:",a)
#             temp=a[j]
#             a[j]=a[j+1]
#             a[j+1]=temp
# print(a)

#print all prime numbers in an interval
#prime number is which is not divisible by any number
# l=2
# u=20
# for i in range(l,u+1): #why we given u+1 is to print upto 20 if not it will print only upto 19
#     if i>1:
#         for n in range (2,i):
#             if i%n==0: #this line prints prime number 
#                        #so we are breaking else it print remaining numbers which is not divisible by any number
#              break
#         else:
#                 print(i)

#display multiplication table
# n=int(input("enter the number:"))
# for i in range(0,10):
#     i=i*n
#     print(i)

#print the fibonacci sequence(0+1=1,1+1=2,1+2=3,2+3=5,3+5=8,5+8=13,.......and so on called fibonacci sequence)
# n=int(input("enter the number:"))
# a=0
# b=1

# for i in range(0,n):
#     if i<=1:
#         c=i
#     else:
#         c=a+b
#         a,b=b,c
#         # a=b
#         # b=c
#         i+=1
#         print(c,end='\t')
        



#check Armstrong number(example:- 153=1^3+5^3+3^3=153 , 1634=1^4+6^4+3^4+4^4=1634)
# n=int(input("enter the number: "))
# order = len(str(n))
# temp=n
# sum=0

# while temp>0:
#     digit=temp%10#1stly given no. is % by 10 so the result is 15.3 remainder,so we are taking 3 1stly
#     sum+=digit ** order#we are cubing the remainder 3 
#     temp//=10 # we are floating the number 15.3/10 so it will remove .3 and give 15 
#              # that 15 will go to while loop and again cube 1 and 5 will give result
# if sum==n:
#  print("it is an armstrong number")
# else:
#  print("it is not an armstrong number")



#find the sum of natural numbers
# n=20
# sum=n*(n+1)/2
# print("sum is: ",sum)

# n=20
# if n<0:
#     print("enter the positive number")
# else:
#     sum=0 #we are storing zero in sum
#     while n>0:  #when n>0 while in this loop 
#         sum=sum+n #we are adding sum and number and that is given to sum,example:-
#                  #example:- n=20,sum=sum+n --> sum=0+20 --> sum=20
#                           # n=19,sum=sum+n --> sum=20+19 --> sum=39 .....and soo on vice versa
#         n=n-1 #here we are subtracting the number like 20,19,18,17,.....etc
#     print(sum)

#print multiplication table
# n=12
# for i in range(1,11):
#     i=i*n
#     print(i)

#program to generate random numbers
# import random
# print(random.randint(1,20))

#program for reversing the element
#method1
# list1=[1,2,3,4,5,6]
# a=list1[::-1]
# print(a)

#method2
#list2=[7,8,9,10,11,12]
#list2.reverse()
#print(list2)

#program to find the file size
# import os
# a=os.stat('clacPrac.py')
# print(a.st_size)

#program to get the class name
# class dog:
#     def name(self,name):
#      return name
# d=dog()
# print(d.__class__.__name__)

#list two strings are anagram
#METHOD1
# name1="listen"
# name2="silent"

# if(sorted(name1)==sorted(name2)):
#    print("this is an anagram")
# else:
#    print("this is not an anagram")

#METHOD2
# n1="listen"
# n2="silent"

# def check(n1,n2):
#    if(sorted(n1)==sorted(n2)):
#       print(n1+" what iam saying "+n2)
#     # is an anagram")
#    else:
#       print("not an anagram")
# check(n1,n2)

#capitalize the first character of a string
# str=("what is your name")
# print(str[0].upper()+ str[1:])
#METHOD2
# # s=str.capitalize()  //it changes the 1st charecter to upper and remaining to lower
# # print(str.upper())

#countdown in python
# import time
# def countdown(time_sec):
#     while time_sec:
#         mins,sec=divmod(time_sec, 60)
#         timeformat='{:02d}:{:02d}'.format(mins, sec)
#         print(timeformat, end='\r')
#         # print(time_sec)
#         time.sleep(1)
#         time_sec-=1
#     print("stop")
# countdown(10)

#iteration
languages = ["C", "Python", "Java", "JavaScript", "Go"]
 
for language in languages:
    print(language)
    


       

    