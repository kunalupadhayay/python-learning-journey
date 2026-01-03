# Age=int(input("enter the age :"))

# if(Age<=13):
#     print("it is a child")
# elif (Age>=13 and Age< 18):
#     print("it is a teenager")
# else :
#     print("adult")


#Q2

# username=input("enter the username:")
# password=input("enter the password:")

# if(username=="kunal" and password=="admin"):
#     print("LOGIN GRANTED!")
# else:
#     if(username !="kunal"):
#         print("wrong username")
#     else:
#         print("wrong password")      

#Q3

# n=int(input("enter the no:"))

# if(n%5==0):
#     print("it is the multiple of 5 ")
# else:
#     print("not multiple of 5 ")


#q4

# n=int(input("enter the number:"))

# if(n%2==0):
#     print("this is the even no")
# else:
#     print("the no is odd")


#///////

# i=1
# while (i<=10):
#     print(6*i)
#     i+=1

#//////

# n=int(input("enter the no :"))

# sum=0

# for i in range (1, n+1):
#     sum += i
# print("count=",sum)


# block of code that perform a specific tast is knows as fn .



#cal sum of three value 

# def sum(a,b,c):
#     s=a+b+c
#     return s/3
# print(sum(10,40,60))


#FACTRIOAL OF N NO 

# def fact(a):
#     n=1
#     for i in range(1,a+1):
#         n *= i

#     return n 
# a=int(input("enter the n:"))
# print(fact(a))    


#####assignment####

#Q1

# salary=int(input("enter the salary:"))

# if (salary<30000):
#     print("cut 5% tax from salary")
# elif(30000 <= salary<=70000):
#     print("cut 15% tax from salary")
# else:
#     print("cut 25% tax from salary")


#q2

# a=int(input("enter the no:"))
# b=int(input("enter the no:"))
# for i in range (a,b+1):
#     if(i%2==0):
#         print(i)

#q

# for i in range (1,101):
#     if(i % 3==0 and i%5==0):
#      print(i)


#Q

# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def multiply(x,y):
#     return x*y
# def divide(x,y):
#     return x/y

# print("select the operation")
# print("1.add")
# print("2.sub")
# print("3.multipy")
# print("4.divide")

# a=input("enter the no:")

# num1=int(input("enter the 1 digit:"))
# num2=int(input("enter the 2 digit:"))

# if a =="1":
#     print(num1,"+",num2,"=",add(num1,num2))
# elif a=="2":
#      print(num1,"-",num2,"=",sub(num1,num2))
# elif a=="3":
#      print(num1,"*",num2,"=",multiply(num1,num2))
# elif a=="4":
#      print(num1,"/",num2,"=",divide(num1,num2))
# else:
#     print("invalid input !!")


#Q


# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# print(is_prime(3))
# print(is_prime(34))


#q

# secret=69

# for i in range (100):
#     guess=int(input("enter the no :"))
#     if guess>secret:
#         print("too high")
#     elif guess<secret:
#         print("too low")
#     else:
#         print("correct!")




