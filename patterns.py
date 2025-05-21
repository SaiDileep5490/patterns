def fun():
    for i in range(0,5):
        for j in range (0,i+1):
            print("*",end = "")
        print()
        
fun()

print()
print()

def fun1():
    for i in range(0,5):
        for j in range(0,5-i):
            print("*",end = "")
        print()
        
fun1()

print()
print()

def fun2():
    for i in range(0,5):
        for j in range(0,5):
            print("*",end = "")
        print()
    
fun2()

print()
print()

def fun3():
    k =0
    for i in range(0,5):
        for j in range(0,k+1):
            print("*",end = "")
        k = k+2 
        print()
        
fun3()

print()
print()

def fun4():
    for i in range(1,5):
        for j in range(1,i+1):
            print(j,end = "")
        print()

fun4()
        
print()
print()

def fun5():
    k =1
    for i in range(0,5):
        for j in range(0,i+1):
            print(k,end= " ")
            k = k+1
        print()
fun5()

print()
print()

def fun7():
    k = ord("A")
    for i in range(0,4):
        for j in range(0,i+1):
            print(chr(k), end = " ")
            k = k+1 
        print()
fun7()
print()
print()

def fun8():
    k = ord("A")
    for i in range(0,4):
        for j in range(0,i+1):
            print(chr(k), end = " ")
        k = k+1 
        print()
fun8()
print()
print()

def fun9():
    n=123
    rev =0
    
    while n>0:
        a = n%10
        rev = rev*10+a
        n = n//10
    print(rev)
fun9()

print()
print()
 
def func10():
    n =4
    for i in range(0,n):
        for j in range(n-i-1):
            print(" ",end="")
        for i in range(i+1):
            print("*",end=" ")
        print()
func10()

print()
print()

def func11():
    n =4
    for i in range(n,0,-1):
        for j in range(n-i):
            print(" ",end="")
        for i in range(i):
            print("*",end=" ")
        print()
func11()

 
    
            

            
    
