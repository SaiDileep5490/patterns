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
    
 
    
            

            
    