def pattern1(n):
    for i in range(n):
        print('* ' * n)


def pattern2(n):
    for i in range(1,n+1):
        print('* ' * i)

def pattern3(n):
    i = 1
    out = ''
    while i <= n:
        out += str(i) + ' '
        print(out)
        i += 1

def pattern4(n):
    for i in range(1, n+1):
        j = str(i)+' '
        print(j*i)

def pattern5(n):       
    for i in range(n,0,-1):
        print('* ' * i)


def pattern6(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
                print(j, end= ' ')
        print()


def pattern7(n):
    i = 1
    j = 1
    while i <= n:
        spaces = n - i
        print(" " * spaces, end='')
        print("* " * j)
        j += 2
        i += 1

def pattern8(n):
    i = n
    j = (n*2)-1
    while i > 0:
        spaces = n - i
        print(" " * spaces, end='')
        print("* " * j)
        j -= 2
        i -= 1


def pattern9(n):
    i = 1
    while i <= n:
        spaces = n - i
        print(' '*spaces, end="")
        print("* "*i)
        i+=1
    i = n
    while i > 0:
        spaces = n - i
        print(' '*spaces, end="")
        print("* "*i)
        i-=1


def pattern10(n):
    for i in range(1,n+1):
        print("* "*i)
    for i in range(n-1,0,-1):
        print("* "*i)


def pattern11(n):
    for i in range(1, n+1):
        if i % 2 == 0: out = 0
        else: out = 1
        for j in range(i):
            print(out, end=' ')
            if out == 1: out = 0
            else: out = 1
        print()

def pattern12(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        spaces = (n*2)-(i*2)
        print("  "*spaces, end="")
        for k in range(i,0,-1):
            print(k, end=" ")
        print()
            
      
def pattern13(n):
    out = 1
    for i in range(1,n+1):
        for j in range(i):
            print(out, end= ' ')
            out += 1
        print()


def pattern14(n):
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        print(char[:i+1])

def pattern15(n):
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n,0,-1):
        print(char[:i])

def pattern16(n):
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        print(char[i]*(i+1))



pattern16(5)
