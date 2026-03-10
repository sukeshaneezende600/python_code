marks = int (input("enter student marks :"))
if( marks >= 90):
    grade ="A"
elif(marks>=90 and marks <90):
    grade= "B" 
elif(marks >=70 and marks <80) :
    grade="C"
else:
    grade= "D"   

print("grade of the student->",grade)     


#Nesting 
age =95
if(age>=18):
    if (age >=80):
        print("cannot drive")
    print("can drive") 
else:
    print("cannot drive")    
    
#WAP to check if a number entered by the user is odd or even.
num = int(input("enter number:"))
rem = num % 2 
if(rem==0):
    print("EVEN")
else:
    print("ODD")    

 #WAP to find the greatest of 3 numbers entered by the user.
    
 
a = int(input("enter the first number:"))
b = int(input("enter second number: "))
c = int(input("enter third number :"))
if (a>=b and a>=c):
    print("first number is greates", a)
elif(b >= c ) :
    print("second is largest number ",b)  
else:
    print("third is greates number", c)   


# WAP TO CHECK IF A NUMBER IS A MULTIPLE OF 7 OR NOT 

a = int(input("enter any number:"))   
if(a % 7 ==0):
    print("multiple of 7")
else:
    print("not a multiple")
  