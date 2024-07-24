# num=int(input("enter a number"))
# x=num%10
# print(x)  # y
'''###################################'''
# x,y=divmod(100,3)
# print("quotion =",x)
# print("remainder=",y)
'''###################################'''
# Tup=(1,2,3,4,5)
# List1=['a','b','c','d','e']
# print(list(zip(Tup,List1)))
# class ABC():
#     def  __init__(self,var):
#         self.var=var
#     def display(self):
#         print("var is = ",self.var)
#     def add_2(self):
#         self.var+=2
#         self.display()
# obj=ABC(10)
# obj.display()
# obj.add_2()
# obj.display()
'''if statement'''
# x=int(input("enter a number :: "))
# if(x>0):
#     x=x+1
# print(x)
'''###################################'''
# age=int(input("enter u r age :: "))
# if(age>=18):
#     print("u r eligible ")
'''###################################'''
# char=input("enter a key ")
# if(char.isalpha()):
#     print("the user has enter a character ")
# if(char.isdigit()):
#     print("the user has enteer a digit ")
'''if else '''
# x=int(input("enter a number "))
# if(x%2==0):
#     print(x,"is a even ")
# else:
#     print(x,"is odd")
'''###################################'''
# x=input("enter a chacter ")
# if(x>='A' and x<='Z'):
#     x=x.lower()
#     print(x)
# else:
#     x=x.upper()
#     print(x)
'''###################################'''
# x=input("enter m or f ")
# sal=int(input(" enter a salary "))
# if(x=='m'):
#     bonus=0.05*sal
# else:
#     bonus=0.10*sal
# amount=bonus+sal
# print(sal)
# print(bonus)
# print(amount)
'''###################################'''
# x=int(input("enter any year "))
# if((x%4==0 and x%100==0) or (x%400==0)):
#     print( x,"is a leaper")
# else:
#     print(x,"not")
'''###################################'''
  # a=int(input("enter a value "))
# b=int(input("enter  bvalue "))
# c=int(input("enter c value "))
# D=(b*b)-(4*a*c)
# deno=2*a
# if(D>0):
#     print("roots are real")
#     r1=(-b+D**0.5)/deno
#     r2=(-b-D**0.5)/deno
#     print("root1 is ",r1)
#     print("root2 is ",r2)
# elif(D==0):
#     print("EQATIONS")
#     r1=-b/deno
#     print("root is ",r1)
# else:
#     print("ImAGINARY")
'''  while loop '''
# m=int(input("enter a m value "))
# n=int(input("enter a n value "))
# s=0
# while(m<=n):
#     s=s+m
#     m=m+1
# print("Sum = ",s)
'''###################################'''
# n=n1=p=p1=z=z1=0
# print("enter -1 to exit ")
# while(1):
#     x=int(input("enter a number "))
#     if(x==-1):
#         break
#     if(x>0):
#         p=p+1
#         p1=p1+x
#     elif(x<0):
#         n=n+1
#         n1=n1+x

#     else:
#         z=z+1

# p1_av=float(p1/p)
# n1_av=float(n1/n)
# print( "no.of +v numbers ",p,p1_av)
# print("no.of -ve numbers is ",n,n1_av)
# print("no.of zeros is ",z)

# n=int(input("enter a number "))
# s=0
# n1=n
# while(n>0):
#     r=n%10
#     s=s+(r**3)
#     n=n/10
# if(s==n1):
#     print("is amstrong")
# else:
#     print("is not ")

'''error occurance'''
# de_n=int(input("enter a decimal number :: "))
# bi_n=0
# i=0
# while(de_n!=0):
#     re=de_n%2
#     bi_n=bi_n+re*(10**i)
#     de_n=de_n/2
#     i=i+1
# print("the biary number :: ",bi_n)



'''error '''

# bi_n=int(input("enter a decimal number :: "))
# de_n=0
# i=0
# while(bi_n!=0):
#     re=bi_n%10
#     de_n=de_n+re*(2**i)
#     bi_n=de_n/10
#     i=i+1
# print("the biary number :: ",de_n)


# x=int(input("enter a number is "))
# sod=0
# while(x!=0):
#     t=x%10
#     sod=sod+t
#     x=x/10
# print("the sum of digits is : ",sod)



# x1=int(input("enter a num "))
# x2=int(input("enter a num  "))
# if(x1>x2):
#     dividend=x1
#     divisor=x2
# else:
#     dividend=x2
#     divisor=x1
# while(divisor!=0):
#     remainder=dividend%divisor
#     dividend=divisor
#     divisor=remainder
# print("gcd is :: ",dividend)



'''error occurance'''
# x=int(input("enter a number :: "))
# print("the reverse ao the number is :: ")
# while(x!=0):
#     t=x%10
#     print(t,end =" ")
#     x=(x/10)


'''for loop
'''
# for i in range(1,20,3):
#     print(i,end=" ")

# x=int(input("enter a numbers  "))
# avg=0
# s=0
# for i in range(1,x+1):
#     s=s+i
# avg=s/i
# print("sun of numbers :: ",s)
# print("avg :: ",avg)

# x=int(input("enter a nkumber "))
# for i in range(1,11):
#     print(x*i)


# m=int(input("enter n value "))
# n=int(input("enter a m value  "))
# for i in range(m,n+1):
#     if(i%2==0):
#         print("even number :: ",i)
#     else:
#         print("odd numbers is :: ",i)


# n=int(input("enter a number :: "))
# if(n==0):
#     fact=1
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("fact= ",fact)


# n=int(input("enter a number "))
# composite=0
# for i in range(2,n):
#     if(n%i==0):
#         composite=1
#         break
# if(composite==1):
#     print("number is composit ")
# else:
#     print("prime number ")


# num=int(input("enter a number "))
# n=int(input("enter a number "))
# result=1
# for i in range(n):
#     result=result*num
# print("power is  ",result)

# m=int(input("enter a number "))
# n=int(input("enter a number "))
# for i in range(m,n+1):
#     if(i%4==0):
#         print(i,end=" ")

# n=int(input("enter a number :: "))
# s=0
# for i in range(1,n+1):
#     a=1/(i**2)          # a=float(i)/(i+1)  ,a=float(i**i)/(i)  
#     s=s+a
#     print("   ",s)


  
# for i in range(1,6):
#     print()
#     for j in range(1,i+1):
#         print(j,end=" ")

# for i in range(1,6):
#     print()
#     for j in range(1,i+1):
#         print(i,end=" ")




'''  functions  '''


# num1=10
# print("globel variable  num1 = ",num1)
# def func(num2):
#     print("in the function local variable num2 = ",num2)
#     num3=30
#     print("the function is local variable  ",num3)
# func(20)
# print("num1 again = ",num1)
# print("num3 otside function = ", num3)

# def rev(x):
#     return x[::-1]
# n=input("enter a string :: ")
# a=rev(n)
# print(a)

# def display(str):
#     print(str)
# x=display("hello world ")
# print(x)
# print(display("hello again "))

# def func(name,*fav_subject):
#     print("\n",name,"likes to read ")
#     for sub in fav_subject:
#         print(sub)
#     # print(*fav_subject)
# func("ravi","maths","ps")
# func("raju","c","DS","DAA")
# func("krish ")



# def small(a,b):
#     if(a<b):
#         return a
#     else:
#         return b
# sum=lambda x,y:x+y
# dif=lambda x,y:x-y
# print("smaller numder is  :: ",small(sum(-3,-4),dif(-9,-4)))


# x=lambda :sum(range(1,100))
# print(x())

# a=lambda x,y:x+y
# b=lambda x,y,z: x*a(y,z)
# print(b(3,4,5))


# def func():
#     """    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
#     fffffffffffffffff  fffffffffffffffff
#     gggggggggggg  gggggggggggggggggggg
#     ccccccccccc  cccccccccccccccccccc  """
#     print("hello ")
# print(func.__doc__)

'''pg=209'''


# def fact(n):
#     f=1
#     if(n==0 or n==1):
#         return 1
#     else:
#         for i in range(1,int(n+1)):
#             f=f*i
#         return f
# n=int(input("enter a n value :: "))
# r=int(input("enter a r value :: "))
# res=float(fact(n))/float(fact(r))
# print("  ",str(res))


'''pending 5.10 in pg 209'''



# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("enter a number :: "))
# print(fact(n))


# def GCD(x,y):
#     rem=x%y
#     if(rem==0):
#         return y
#     else:
#         return GCD(y,rem)
# n=int(input(" enter a n value :: "))
# m=int(input("enter a m value :: "))
# print(GCD(n,m))


# def exp(x,y):
#     if(y==0):
#         return 1
#     else:
#         return(x*exp(x,y-1))
# n=int(input("enter a n value :: "))
# m=int(input("enter a m value :: "))
# print(exp(n,m))


# def fib(n):
#     if(n<2):
#         return 1
#     else:
#         return (fib(n-1)+fib(n-2))
# n=int(input("ener a number ::: "))
# for i in range(n):
#     print(i, fib(i))


# from math import sqrt as sq
# print(sq(81))

"""error occur"""

# def lar(a,b):
#     if(a>b):
#         return a
#     else:
#         return b
# import MyModule
# print(MyModule.lar(50,100))
# print(MyModule.lar('B','C'))
# print(MyModule.lar('HI','BY'))
# print(MyModule.lar(50,100))

# import calendar
# print(calendar.month(2017,1))


# import datetime
''''#### strings ######'''
# def remove(s):
#     new_str=""
#     for i in s:
#         if i in "aeiouAEIOU":
#             pass
#         else:
#             new_str+=i
#     print(" the string without ovals is :: ",new_str)
# str=input("enter a string  ")
# remove(str)
'''#########################################'''
# def find(s,c):
#     index=0
#     while(index<len(str)):
#         if s[index]==c:
#             print("found at :: ",index)
#             return
#         else:
#             pass
#         index+=1
#     print("not found :: ")
# str=input("enter a string :: ")
# ch=input("enter a character :: ")
# find(str,ch)

'''############## 6.8###########'''

# def count_ch(s,c):
#     cou=0
#     for i in s:
#         if i ==c:
#             cou+=1
#     return cou
# str=input("enter the string :: ")
# ch=input("enter a character :: ")
# cou=count_ch(str,ch)
# print("in",str,ch,"occur ",cou,"times")
'''#########################'''
# def count_ch(s,c,beg=0):
#     count=0
#     index=beg
#     while(index<len(s)):
#         if s[index]==c:
#             count+=1
#         index+=1
#     return count
# str=input("enter a string :: ")
# ch=input("enter a character :: ")
# count=count_ch(str,ch)
# print("in",str,ch,"occurs ",count,"times from begin")
# loc=int(input("enter a position to start :: "))
# count=count_ch(str,ch,loc)
# print("in",str,ch,"occurs ",count,"times from position",loc,"to end")
'''#####################################'''
# def reverse(str):
#     x=''
#     i=len(str)-1
#     while(i>=0):
#         x+=str[i]
#         i-=1
#     return x
# str=input("inter a string :: ")
# print("the reverse of a string is ::: ",reverse(str))
'''#####################<------ files --->######################################'''
# file=open("File.txt","wb")
# print("Name of the file :: ",file.name)
# print("File is closed :: ",file.closed)
'''###############################'''
# file=open("File.txt","r")
# #lines='irfan'
# a=file.readlines()
# print(a[0])
# file.close()
# print("data was written ")
'''###############################'''
# file=open("File.txt","a")
# file.write("\n python is very simple and power lan ")
# file.close()
# print("data append to a file ")
'''#########################'''
# file=open("File.txt","r")
# print("first line is read ::- ",file.readline())
# print("second line is read ::-  ",file.readline())
# print("third line is read ::- ",file.readline())
'''#################################'''
# with open("File.txt","r") as file:
#     print(file.read())
# file.close()
'''##############################'''
# with open("File.txt","r")as file:
#     x=file.readline()
#     y=x.split()
#     print(y)
'''#################################'''
# with open("File.txt","rb")as file:
#     with open("File2.txt","wb")as file2:
#         x=file.read()
#         file2.write(x)
# print("file copied ")
'''###################'''
# x=input("enter  a file name :: ")
# with open(x)as file:
#     txt=file.read()
#     le=input("enter a letter which find :: ")
#     count=0
#     for char in txt:
#         if char==le:
#             count+=1
# print(le,"appersk",count,"times in file ")
'''################################'''
# x=input("enter a file name :: ")
# with open(x)as file:
#     txt=file.read()
#     count_vo=0
#     count_co=0
#     for char in txt:
#         if char in "aeiouAEIOU":
#             count_vo+=1
#         else:
#             count_co+=1
# print("no of vovels is ",count_vo)
# print("no of consonent is ",count_co)
# print("total no of words :: ",len(txt))
# print("percentage of vovels :: ",((count_vo)*100)/len(txt),"%")
# print("percentage of consonents :: ",((count_co)*100)/len(txt),"%")
'''######################################################'''
# import os
# path="D:\PYTHON"
# filename="File.txt"
# abs_path=os.path.join(path,filename)
# print("file name is :: ",abs_path)
# file=open(abs_path,"w")
# file.write("hi how r u ")
# file.close()
# file=open(abs_path,"r")
# print(file.read())
'''################  307 to 311  '''
'''##################### DATA STRU     #######################'''
# x=[i**3 for i in range(11)]
# print(x)
'''##########################################'''
# print([(x,y) for x in [10,20,30] for y in [30,10,20] if x!=y ])
# x=[1,23,34,5,6]
# s=0
# for i in x:
#     s+=i
# print("sum of the numbers :: ",s)
# print("avg =", s/float(len(x)))
'''###################################33333'''
# x=[4,5,6,7,8,9,0,1,2,3]
# for index,i in enumerate(x):
#     print(i,"is at index : ",index)
'''#############################################'''
# def check(x):
#     if(x%2==0 or x%4==0):
#         return 1
# print(list(filter(check,range(2,200))))
'''###############################################'''
# def add2(x):
#     x+=2
#     return x
# y=[4,3,6,2,3,6,1]
# print(y)
# print(list(map(add2,y)))
'''######################################################'''
# import functools
# def add(x,y):
#     return x+y
# n1=[4,5,3,6,7,8]
# print(functools.reduce(add,n1))
'''################################################'''
# div_2_4=[]
# for i in range(2,22):
#     if i%2==0 or i%4==0:
#         div_2_4.append(i)
# print(div_2_4)
'''########################################'''
# def squ(x):
#     return(x**2)
# s=[]
# s=list(filter(squ,range(1,10)))
# print(s)
# sum=0
# for i in s:
#     sum+=i
# print(sum)
'''####################################################'''
# x=[]
# for i in range(1,10):
#     x.append(i)
# print(x)
# for indx,i in enumerate(x):
#     if i%2==0:
#         del x[indx]
# print(x)
'''##########################################'''
'''error occur pg 339'''
# x=[1,2,3,4,5,4,3,2,1]
# y=input("enter a character :: ")
# i=0
# cunt=0
# while i<len(x):
#     if y==x[i]:
#         print(y," found at", i)
#         cunt+=1
#     i +=1
# print(y,"appears ",cunt, "times ")
'''#############################################'''
# x=[1,2,3,4,5,6,7,6,5,4]
# print(x)
# i=0
# while i<len(x):
#     y=x[i]
#     for j in range(i+1,len(x)):
#         z=x[j]
#         if y==z:
#             x.pop(j)
#     i+=1
# print(x)
'''####################################'''
# x=[]
# m=int(input("enter a starting of range :: "))
# n=int(input("enter a srting in range :: "))
# o=int(input("enter a step of a number :: "))
# for i in range(m,n,o):
#     x.append(i)
# print(x)
# x.reverse()
# print(x)
'''###################################'''
# x=[]
# ev=[]
# odd=[]
# for i in range(10):
#     x.append(i)
# print(x)
# for i in range(len(x)):
#     if i%2==0:
#         ev.append(i)
#     else:
#         odd.append(i)
# print(ev)
# print(odd)
'''#########################################'''
# def positive(x):
#     if x>=0:
#         return x
# li=[10,-20,30,-40,50,-60,70,-80,90,-100]
# li=list(filter(positive,li))
# print(li)
'''#################################################'''
# print([(x,y) for x in [10,20,30,50] for y in [35,40,55,60] if y%x==0 or x%y==0])
'''###############################################################################'''
'''error occur '''
# def con_fa(cel):
#     return ((float(9/5)*tem_cel+32))
# tem_cel=(36.5,37,37.5,39)
# tem_fa=list(map(con_fa,tem_cel))
# print(tem_cel)
# print(tem_fa)
'''#############################################'''
# import functools
# def max_num(x,y):
#     return x>y
# num_list=[4,1,8,2,9,3,0]
# print(functools.reduce(max,num_list))
'''#######################################################'''
# a=0
# b=1
# i=2
# n=int(input("enter a no.of terms :: "))
# list[a,b]
# while i<n:
#   s=a+b
#   list.append(s)
#   a=b
#   b=s
#   i+=1
# print(list)
# i=0
# s1=0
# while i<n:
#   s1+=list[i]
#   i+=2
# print(s1)
'''#############################################################'''
# x=[[2,5,4],
#   [1,3,9],
#   [7,6,2]]
# y=[[1,8,5],
#   [7,3,6],
#   [4,0,9]]
# re=[[0,0,0],
#    [0,0,0],
#    [0,0,0]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         re[i][j]=x[i][j]+y[i][j]
# for r in re:
#     print(r)
'''#################################################'''
# l=[]
# n=int(input("eneter a size :: "))
# for i in range(n):
#   print("enter numbers ",i+1, ":")
#   num=int(input())
#   l.append(num)
# print("sorted :: ")
# l=sorted(l)
# print(l)
# i=len(l)-1
# if n%2!=0:
#   print(l[i//2])
# else:
#   print((l[i//2]+l[i+1//2])/2)
'''########################################'''
'''tuples '''
# r,q=divmod(100,3)
# print(r)
# print(q)
'''#################################'''
# def num(val):
#   x=max(val)
#   y=min(val)
#   z=len(val)
#   return (x,y,z)
# val=(99,98,90,97,89,86,93,82)
# (max_marks,min_marks,len_marks)=num(val)
# print(max_marks)
# print(min_marks)
# print(len_marks)
'''###############################'''
# tup=(1,2,3,4,5)
# li=['a','b','c','d','e']
# print(list(zip(tup,li)))
'''############################'''
# tup=[(1,'a'),(2,'b'),(3,'c'),(4,'d')]
# for i,char in tup:
#     print(i,char)
'''############################'''
# for index,ele in enumerate('abcdefg'):
#     print(index,ele)
'''##############################'''
# tup=("heena ",89,82.4)
# print("%s got %d marks in CSA and her a %.2f "%(tup[0],tup[1],tup[2]))
'''#################################################'''
# pi=3.14
# def cir(r):
#     return (pi*r*r,2*pi*r)
# radius=float(input("enter a radius :: "))
# (area,cu)=cir(radius)
# print(area," :: ",cu)
'''#########################'''
# toper=(("arvin ","bsc ",92.0),("chandu ","bca ",99.0),("danu ","btech ",97))
# for i in toper:
#   print(i)
# choice=input("enter which u eddit :: ")
# if choice=='y':
#   name=input("enter a name which u will be edit :: ")
#   new_name=input("enter a name :: ")
#   new_course=input("enter a course :: ")
#   new_aggr=input("enter a correct aggre :: ")
#   i=0
#   new_toper=()
#   while i<len(toper):
#     if toper[i][0]==name:
#       new_toper+=(new_name,new_course,new_aggr)
#     else:
#       new_toper+=toper[i]
#     i+=1
# for i in new_toper:
#   print(i,end=" ")  
'''#####################################'''
# addr='abc@gmail.com'
# name,dname=addr.split('@')
# print(name)
# print(dname)
'''###########################'''
# def sum(*args):
#   tot=0
#   for i in args:
#     if i>0:
#       tot+=i
#   return tot
# print(sum(1,-9,2,-8,3,-7,4,-6,5))
'''##############################'''
# ques=["roll_no ","name ","course "]
# ans=[7,"rahul ","bbs "]
# for q,a in zip(ques,ans):
#     print( "what is u r name :: ",q,"?")
#     print("my ",q," is :: ",a)
'''###########################'''
# odd =set([x*2+1 for x in range(1,10)])
# print(odd)
# prime=set()
# for i in range(2,20):
#   j=2
#   flag=0
#   while j<i/2:
#     if j%i==0:
#       flag=1
#     j+=1
#   if flag==0:
#     prime.add(i)
# print(prime)
# print(odd.union(prime))
# print(odd.intersection(prime))
# print(odd.symmetric_difference(prime))
# print(odd.difference(prime))
'''##########################'''
# even=set([x*2 for x in range(1,10)])
# print(even)
# comp=set()
# for i in range(2,20):
#   j=2
#   flag=0
#   while j<=i/2:
#     if i%j==0:
#       comp.add(i)
#     j+=1
# print(comp)
# print(even.issuperset(comp))
# print(all(even))
# print(len(comp))
# print(sum(even))
'''##############################'''
# sq=([x**2]) pg=366
'''############ Dictionary ##############'''
# dict={'roll_no':'16/001','name':'A','course':'btech'}
# print(sorted(dict.keys()))
'''##########################'''
# d={'roll':'123','name':'abc','course':'btech'}
# print(d)
# for key in d:
#   print(key)
# for val in d.values():
#   print(val)
# for key,val in d.items():
#   print(key,val)
'''#############################'''
# st={'A':{'cs':90,'ds':89,'ca':92},'B':{'cs':92,'ds':81,'ca':97},'C':{'cs':94,'ds':85,'ca':96}}
# for key,val in st.items():
#   print(key,val)
'''###########################'''
# print(" -1 ")
# circu={}
# while True:
#     r=float(input(" rabius :: "))
#     if r==-1:
#       break
#     else:
#        d={r:2*3.14*r}
#        circu.update(d)
# print(circu)
'''######################'''
# m_cm={x:x*100 for x in range(1,11)}
# tem=m_cm.values()
# cm_m={x:x/100 for x in tem}
# print(m_cm," :: ",cm_m)
'''############################'''
# D={0:0,1:1}
# def fib(n):
#   if n not in D:
#     val=fib(n-1)+fib(n-2)
#     D[n]=val
#   return D[n]
# n=int(input("enter a value :: "))
# print(fib(n))
'''##########################'''
# def cou(mess):
#   x={}
#   for y in mess:
#     x[y]=x.get(y,0)+1
#   print(x)
# mess=input("enter a message :: ")
# cou(mess)
'''########################'''
# matr=[[0,0,0,1,0],
#       [2,0,0,0,3],
#       [0,0,0,4,0]]
# d={}
# print("spare matrix :: ")
# for i in range(len(matr)):
#   print("\n")
#   for j in range(len(matr[i])):
#     print(matr[i][j],end="  ")
#     if matr[i][j]!=0:
#       d[i,j]=matr[i][j]
# print("\n\n :: ")
# print(d)
'''####################'''
# D={'roll':1,'name ':'A','course':'btech'}
# inv={}
# for k,v in D.items():
#   inv[v]=k
# print(inv)        
'''######################'''
# marks={'neha ':[97,89,94,90],'mitu':[92,91,94,87],'sht':[67,99,88,90]}
# tot=0
# totmarks=marks.copy()
# for k,v in marks.items():
#   tot=sum(v)
#   totmarks[k]=tot
# print(totmarks)
# max=0
# top=' '
# for k,v in totmarks.items():
#   if v>max:
#     max=v
#     top=k
# print(top,max)
'''########################'''
# msg='hello all good morning welcome to the world of python '
# msg=msg.lower()
# D=dict()
# for word in msg:
#   if word not in D:
#     D[word]=1
#   else:
#     D[word]=D[word]+1
# print(D)
# for k,v in D.items():
#   print(k,'\t','*' * v)
'''#############################'''
# filename=input("enter a file name :: ")
# file=open(filename)
# coun=dict()
# for line in file:
#   wor=line.split()
#   for wo in wor:
#     if wo not in coun:
#       coun[wo]=1
#     else:
#       coun[wo]+=1
# print(coun)
'''###### Iterator and generator ####################'''
# class Iterator:
#   def __init__(self,string):
#     self.string=string
#     self.index=0
#   def __iter__(self):
#     return self
#   def __next__(self):
#     if self.index>=len(self.string):
#       raise StopIteration
#     string=self.string[self.index]
#     self.index+=1
#     return string
# it =Iterator("hello world ")
# for ch in it:
#   print(ch,end=" ")
'''########################'''
''' erroe '''
# class Square:
#   def __init__(self):
#     self.val=0
#   def __iter__(self):
#     return self
# def __next__(self):
#   self.val+=1
#   return self.val**2
# Sq=Square()
# cou=0
# for num in Sq:
#     print(num,end=" ")
#     if cou==10:
#         break
#     cou+=1
'''########################'''
# class odd:
#   def __iter__(self):
#     self.val=1
#     return self
#   def __next__(self):
#     val=self.val
#     self.val+=2
#     return val
# o=odd()
# for i in o:
#   print(next(o),end=" ")
#   if o.val==21:
#     break
'''##############################'''
# def fib():
#   a,b=0,1
#   while a<n:
#     yield b
#     a,b=b,a+b
# it=fib()
# n=int(input("enter a number :: "))
# for i in it:
#   print(i,end=" ") 
'''##########################'''
# def rev(mes):
#   le=len(mes)
#   for i in range(le-1,-1,-1):
#     yield mes[i]
# mes="hello"
# for ch in rev(mes):
#   print(ch,end=" ")
'''############## class and objects ##################'''
# class number:
#   even=[]
#   odd=[] 
#   def __init__(self,num):
#     self.num=num
#     if num%2==0:
#       number.even.append(num)
#     else:
#       number.odd.append(num)
# n1=number(21)
# n2=number(32)
# n3=number(43)
# n4=number(54)
# print(number.even)
# print(number.odd)
'''#################'''
# def scale(x):
#   return x*10
# class abc:
#   def __init__(self,var):
#     self.var=var
#   def display(self):
#     print(self.var)
#   def modi(self):
#     self.var=scale(self.var)
# obj=abc(10)
# obj.display()
# obj.modi()
# obj.display()
'''###############################'''
# class abc:
#   def __init__(self,var):
#     self.var=var
#   def display(self):
#     print(self.var)
# o=abc(10)
# o.display()
# o.new=20
# print(o.new)
# o.new=30
# print(o.new)
'''###########################'''
# class abc:
#   def __init__(self,var1,var2):
#     self.var1=var1
#     self.var2=var2
#   def display(self):
#     print(self.var1)
#     print(self.var2)
# o=abc(10,12.34)
# o.display()
# print(o.__dict__)
# print(o.__doc__)
# print(o.__module__)
'''#########################'''
# class student:
#   def __init__(self,name):
#     self.name=name
#     self.marks=[]
#   def enmarks(self):
#     for i in range(3):
#       m=int(input("enter a marks of %s in sub %d :: "%(self.name,i+1)))
#       self.marks.append(m)
#   def display(self):
#     print(self.name, " ",self.marks)
# s1=student("anes")
# s1.enmarks()
# s2=student("rahul ")
# s2.enmarks()
# s1.display()
# s2.display()   
'''#######################'''
# class emp:
#   empcount=0
#   def __init__(self,name,desig,sala):
#     self.name=name
#     self.desig=desig
#     self.sala=sala
#     emp.empcount+=1
#   def display1(self):
#     print("the %d employe "%emp.empcount)
#   def display2(self):
#     print("",self.name ,self.desig, self.sala)
# e1=emp('far ',"man",100)
# e2=emp("mik","lea ",9)
# e3=emp("niy ","proo",8)
# e4=emp("oj","off ",6)
# e4.display1()
# e2.display2()
'''####################'''
# class circl:
#   pi=3.14
#   def __init__(self,r):
#     self.r=r
#   def area(self):
#     return circl.pi*self.r*self.r
#   def ci(self):
#     return 2*circl.pi*self.r*self.r
# c=circl(7.5)
# print(c.area())
# print(c.ci())
'''###################################'''

'''###########################'''
# class rec:
#   def get(self):
#     rec.len=int(input("enter a length :: "))
#     rec.bre=int(input("enter a breadth :: "))
#   def meas(self):
#     print(rec.len," :: ",rec.bre)
#   def area(self):
#     print(rec.len*rec.bre)
# r=rec()
# r.get()
# r.meas()
# r.area()
'''############################'''
# class stu:
#   mar=[]
#   def set(self,r,n,m1,m2,m3):
#     stu.roll=r
#     stu.name=n
#     stu.mar.append(m1)
#     stu.mar.append(m2)
#     stu.mar.append(m3)
#   def display(self):
#     print(stu.roll)
#     print(stu.name)
#     print(self.total())
#   def total(self):
#     m=stu.mar
#     return m[0]+m[1]+m[2]
# r=int(input("enter a roll no :: "))
# n=input("enter a name ::: ")
# m1=int(input("enter a first marks :: "))
# m2=int(input("enter a first marks :: "))
# m3=int(input("enter a first marks :: "))
# s1=stu()
# s1.set(r,n,m1,m2,m3)
# s1.display()
'''###################'''
# class fra:
#   def get(self):
#     self.num=int(input("enter numsrator :: "))
#     self.deno=int(input("enter a dinominatro :: "))
#     if(self.deno==0):
#       print("not possible :: ")
#       exit()
#   def display(self):
#     self.simplfy()
#     print(self.num,"/",self.deno)
#   def simplfy(self):
#     common_divisor=self.GCD(self.num,self.deno)
#     self.num=self.num/common_divisor
#     self.deno=self.deno/common_divisor
#   def GCD(self,a,b):
#     if (b==0):
#       return a
#     else:
#       return self.GCD(b,a%b)
# f=fra()
# f.get()
# f.display()
'''###############################'''
# class store:
#   itecode=[]
#   price=[]
#   def get(self):
#     for i in range(5):
#       self.itecode.append(int(input("entre the code of iteam :: ")))
#       self.price.append(int(input("enter a price of a iteam :: ")))
#   def display(self):
#     print("iteam code \t price ")
#     for i in range(5):
#       print(self.itecode[i],"\t\t",self.price[i])
#   def cal_bil(self,quant):
#     tot=0
#     for i in range(5):
#       tot+=self.price[i]*quant[i]
#     print("**************bill*************")
#     print("iteam \t price \t qantity \t subtotal ")
#     for i in range(5):
#       print(self.itecode[i] ,"\t",self.price[i], "\t" ,quant[i] ,"\t",quant[i]*self.price[i])
#     print("***************************************")
#     print(tot)
# s=store()
# s.get()
# s.display()
# q=[]
# print(" enter qantity of each iteam :: ")
# for i in range(5):
#   q.append(int(input("enter ")))
# s.cal_bil(q)
'''#######################'''
# class strin:
#   def __init__(self):
#     self.vow=0
#     self.space=0
#     self.conso=0
#     self.upper=0
#     self.lower=0
#     self.string=str(input("enter a string :: "))
#   def couvow(self):
#     for letter in self.string:
#       if(letter in ('a','e','i','o','u')):
#         self.vow+=1
#       elif(letter in ('A','E','I','O','U')):
#         self.vow+=1
#   def couspace(self):
#     for letter in self.string:
#       if(letter==' '):
#         self.space+=1
#   def coucons(self):
#     for letter in self.string:
#       if (letter not in ('a','e','i','o','u','A','E','I','O','U')):
#         self.conso+=1
#   def couupper(self):
#     for letter in self.string:
#       if(letter.isupper()):
#         self.upper+=1
#   def couloweer(self):
#     for letter in self.string:
#       if(letter.islower()):
#         self.lower+=1
#   def comput(self):
#     self.couvow()
#     self.couspace()
#     self.coucons()
#     self.couupper()
#     self.couloweer()
#   def show(self):
#     print(" vowels :: %d "%self.vow)
#     print(" consonents :: %d "%self.conso)
#     print(" space :: %d "%self.space)
#     print(" upper :: %d "%self.upper)
#     print(" lower :: %d "%self.lower)
# s=strin()
# s.comput()
# s.show()
'''##########################'''
'''error occur'''
# import datetime
# class product:
#   def __init__(self):
#     self.manfac=datetime.datetime.strptime(input("entr a manufacture time  :: (mm/dd/yy) "),'%m/%d/%y')     
#     self.expe=datetime.datetime.strptime(input("entr a expiry date :: (mm/dd/yy)",'%m/%d/%y'))
#   def timetoexpar(self):
#     today=datetime.datetime.now()
#     if(today>self.expe):
#       print(" dont buy ")
#     else:
#       timeleft=self.expe.date()-datetime.datetime.now().date()
#       print("time left :: ",timeleft)
#   def show(self):
#     print("expiry :: ",self.expe)
#     print("manfatue time :: ",self.manfac)
# p=product()
# p.timetoexpar()
'''##################################'''
# class acco:
#   def __init__(self):
#     self.balance=0
#     print("account create :: ")
#   def depo(self):
#     amou=float(input("enter a amount to be dposite  :: "))
#     self.balance+=amou
#     print("new balance :: %f"%self.balance)
#   def withdraw(self):
#     amou=float(input("enter a amount to be withdraw :: "))
#     if(amou>self.balance):
#       print("insufficient balance :: ")
#     else:
#       self.balance-=amou
#       print("new balance :: %f"%self.balance)
#   def enquiry(self):
#     print("balance : %f"%self.balance)
# a=acco()
# a.depo()
# a.withdraw()
# a.enquiry()/
'''######################################################'''
# class book:
#   def __init__(self):
#     self.tile=""
#     self.author=""
#     self.price=0
#   def read(self):
#     self.tile=input("entr a book title :: ")
#     self.author=input("enter a auther name :: ")
#     self.price=float(input("enter a price :: "))
#   def display(self):
#     print("title  ",self.tile)
#     print("quthir  ",self.author)
#     print("price  ",self.price) 
#     print("\n")
# mybook=[]
# ch='y'
# while(ch=='y'):
#   print(''' 1.add new book 
#         2.display book
#         ''')
#   choi=int(input("enter choice :: "))
#   if(choi==1):
#     b=book()
#     b.read()
#     mybook.append(b)
#   elif(choi==2):
#     for i in mybook:
#       i.display()
#     else:
#       print("invalid choice :: ")
#     ch=input("do u want to continue ::: ")
# print('bye ')
'''############## inheritance ############'''

'''#### multi level inheri ####'''
# class base1(object):
#   def __init__(self):
#     super(base1,self).__init__()
#     print(" base1 ")
# class base2(object):
#   def __init__(self):
#     super(base2,self).__init__()
#     print("basea2,class ")
# class drive(base1,base2):
#   def __init__(self):
#     super(drive,self).__init__()
#     print("derive class ")
# d=drive()
'''######## multi level ###############'''
# class person:
#   def name(self):
#     print("name ")
# class teach(person):
#   def quali(self):
#     print("phd")
# class hod(teach):
#   def exper(self):
#     print("15 years  ")
# h=hod()
# h.name()
# h.quali()
# h.exper()
'''##### multi path #######'''
# class stu:
#   def name(self):
#     print("namae ")
# class acad(stu):
#   def score(self):
#     print(" 60% ")
# class eca(stu):
#   def sco(self):
#     print(" 90% ")
# class res(acad,eca):
#   def eli(self):
#     print(" elig ")
#     self.score()
#     self.sco()
# r=res()
# r.eli()
'''########################'''
# class poi:
#   def __init__(self,x,y):
#     self.x=x
#     self.y=y
#   def get(self):
#     return (self.x,self.y)
# class loc:
#   def __init__(self,y1,x1,x2,y2):
#     self.sour=poi(x1,y1)
#     self.des=poi(x2,y2)
#   def show(self):
#     print("source :: ",self.sour.get())
#     print("destination :: ",self.des.get())
#   def ref(self):
#     self.des.x=-self.des.x
#     print("reflaction :: ",self.des.x,self.des.y)
# l=loc(1,2,3,4)
# l.show()
# l.ref()
'''########################'''
# class stu:
#   def __init__(self,name,roll,cour,year):
#     self.name=name
#     self.roll=roll
#     self.cour=cou(cour,year)
#   def show(self):
#     print(self.name,self.roll)
#     print(self.cour.get())
# class cou:
#   def __init__(self,name,year):
#     self.name=name
#     self.year=year
#   def get(self):
#     return (self.name,self.year)
# class dep:
#   def __init__(self,name):
#     self.name=name
#     self.cour=[]
#   def get(self):
#     return (name,cour)
#   def add(self,name):
#     self.cour.append(name)
#   def showc(self):
#     print("department courses :: ",self.cour)
# d1=dep("maths ")
# d2=dep("compu ")
# d1.add("ba(h)")
# d1.add("dsc(h)")
# d2.add("bca")
# d2.add("btech ")
# print("***********************************")
# d1.showc()
# d2.showc()
# s=stu("har ",223,"bca ",2017)
# s.show()
'''###########################'''
# class poly:
#   def d(self):
#     raise NotImplementedError()
#   def area(self):
#     raise NotImplementedError()
# class rec:
#   def d(self):
#     self.len=float(input("enter a length of rectangle :: "))
#     self.be=float(input("entre a dreath :: " ))
#   def area(self):
#     return self.len*self.be
# class tri:
#   def d(self):
#     self.base=float(input("entre a basse of tri :: "))
#     self.hei=float(input("enter a height of triangke :: "))
#   def area(self):
#     return 0.5*self.base*self.hei
# r=rec()
# r.d()
# print("rea of rectangle :: ",r.area())
# t=tri()
# t.d()
# print("area of triangle :: ",t.area())
'''#############################'''
# class bill:
#   def __init__(self,itm,pri):
#     self.tot=0
#     self.itm=itm
#     self.pri=pri
#     for i in pri:
#       self.tot+=i
#   def dis(self):
#     print("\n ITEAMS\t\t\t PRICE ")
#     for i in range(len(self.itm)):
#       print(self.itm[i], "\t",self.pri[i])
#       print("********************************0")
#       print("total :: ",self.tot)
# class capay(bill):
#   def __init__(self, itm, pri,deno,val):
#     bill.__init__(self,itm, pri)
#     self.deno=deno
#     self.val=val
#   def s1(self):
#     bill.dis(self)
#     for i in range(len(deno)):
#       print(deno[i],"*",val[i],"=",deno[i]*val[i])
# class chpay(bill):
#   def __init__(self, itm, pri,cno,name):
#     bill.__init__(self,itm, pri)
#     self.cno=cno
#     self.name=name
#   def s2(self):
#     bill.dis(self)
#     print("check number :: ",self.cno)
#     print("bank name :: ",self.name)
# itm=["external ","ram ","printer ","pan drive"]
# pri=[5000,2000,6000,800]
# op=int(input("would you like to pay by cheque or cash (1/2)"))
# if(op==1):
#   nam=input("enter a bank name :: ") 
#   cno=input("enter a check number :: ")
#   chp=chpay(itm,pri,cno,nam)
#   chp.s2()
# else:
#   deno=[10,20,50,100,500,2000]
#   val=[1,1,1,20,4,5]
#   cp=capay(itm,pri,deno,val)
#   cp.s1()
'''###########################################'''
# class pers:
#   def __init__(self,name,age,sex):
#     self.name=name
#     self.age=age
#     self.sex=sex
#   def disp(self):
#     print("name :: ",self.name)
#     print("age :: ",self.age)
#     print("sex :: ",self.sex)
# class publi:
#   def __init__(self,norp,nobook,noart):
#     self.norp=norp
#     self.nobook=nobook
#     self.noart=noart
#   def disp(self):
#     print("no.of reach papers publish :: ",self.norp)
#     print("no of books pub :: ",self.nobook)
#     print("no of arts :: ",self.noart)
# class fac(pers):
#   def __init__(self, name, age, sex,desi,dep,norp,nobook,noart):
#     pers.__init__(self,name, age, sex)
#     self.desi=desi
#     self.dep=dep
#     self.pub=publi(norp,nobook,noart)
#   def disp(self):
#     pers.disp(self)
#     print("designation :: ",self.desi)
#     print("department :: ",self.dep)
#     self.pub.disp()
# f=fac("pooja",38,"female","tic","computer","scince",22,1,3)
# f.disp()
'''##################### over loading ########################'''
'''error pg 462 '''
# class complex:                                                                                       
#   def __init__(self):
#     self.real=0
#     self.ima=0
#   def val(self,real,ima):
#     self.real=real
#     self.ima=ima
#   def __add__(self,c):   # the __add__() must be used for adding two odjects c3=c1+c2
#     t=complex()
#     t.real=self.real+c.real
#     t.ima=self.ima+c.ima
#     return t
#   def x(self):
#     print("(",self.real, "+",self.ima,"i)")
# c1=complex()
# c1.val(1,2)
# c2=complex()
# c2.val(3,4)
# c3=complex()
# c3=c1 + c2
# print("result = ")
# c3.x()
'''##################################'''
# class stud:
#   def __init__(self,name,marks):
#     self.name=name
#     self.marks=marks
#   def dis(self):
#     print(self.name, self.marks)
#   def __add__(self,s):
#     t=stud(s.name,[])
#     for i in range(len(self.marks)):
#       t.marks.append(self.marks[i]+s.marks[i])
#     return t
# s1=stud("nik ",[43,45,33,32,22])
# s2=stud("nik ",[45,44,32,67,89,00],)
# s1.dis()
# s2.dis()
# s3=stud("",[])
# s3=s1+s2
# s3.dis()
'''#############################'''
# class matr:
#   def __init__(self,list):
#     self.list=list
#   def dis(self):
#     print(self.list)
#   def __add__(self,m):
#     t=matr([])
#     for i in range(len(self.list)):
#       for j in range(len(self.list[0])):
#         t.list.append(self.list[i][j]+m.list[i][j])
#     return t
# m1=matr([[1,2],[3,4]])
# m2=matr([[3,4],[5,1]])
# m3=matr([])
# m3=m1+m2
# m1.dis()
# m2.dis()
# print(" result matrix :: ")
# m3.dis()
'''##############################'''
def GCD(num,deno):
  if(deno==0):
    return num
  else:
    return GCD(deno,num%deno)
class frac:
  def __init__(self):
    self.num=0
    self.deno=1
  def get(self):
    self.num=int(input("enter a numerator :: "))
    self.deno=int(input("enter a denomnator :: "))
  def simp(self):
    divsior=GCD(self.num,self.deno)
    self.num//=divsior
    self.deno//=divsior
  def __add__(self,f):
    t=frac()
    t.num=(self.num*f.deno)+(f.num*self.deno)
    t.deno=self.deno*f.deno
    return t
  def dis(self):
    self.simp()
    print(self.num,"/",self.deno)
f1=frac()
f1.get()
f2=frac()
f2.get()
f3=frac()
f3=f1+f2
f3.dis()
























































