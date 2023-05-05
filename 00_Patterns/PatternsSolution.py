print("Star Patterns")

def one():
    print("1.")
    for i in range(5):
        for j in range(5):
            print("* ", end = "")
        print("\n", end = "")

one()

def two():
    print("2.")
    for i in range(1,5+1):
        for j in range(1,i+1):
            print("* ", end = "")
        print("\n", end = "")

two()

def three():
    print("3.")
    for i in range(5,0,-1):
        for j in range(1,i+1):
            print("* ", end = "")
        print("\n", end = "")

three()

def four():
    print("4.")
    for i in range(1,5+1):
        for k in range(1,(5-i)+1):
            print("  ", end  = "")
        for j in range(1,i+1):
            print("* ", end = "")
        print("\n", end = "")

four()

def five():
    print("5.")
    for i in range(5,0,-1):
        for k in range(1,(5-i)+1):
            print("  ", end  = "")
        for j in range(1,i+1):
            print("* ", end = "")
        print("\n", end = "")

five()

def six():
    print("6.")
    space = 0
    for i in range(5,0,-1):
        for k in range(1,space+1):
            print("  ", end  = "")
        space = space + 2
        for j in range(1,i+1):
            print("* ", end = "")
        print("\n", end = "")

six()

def seven():
    print("7.")
    for i in range(1,6):
        if i in range(2,(5-1)+1):
            for j in range(1,5+1):
                if j==1 or j==5:
                    print("* ", end = "")
                else:
                    print("  ", end = "")
        else:
            for j in range(1,5+1):
                print("* ", end = "")    
        print("\n", end = "")

seven()

def eight():
    print("8.")
    n=5
    f=1
    l=n
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==f or j==l:
                print("* ", end = "")
            else:
                print("  ", end = "")
        f = f + 1
        l = l - 1
        print("\n", end = "")

eight()

def nine():
    print("9.")
    mid = int(9/2) + 1
    f=mid
    l=mid
    flag = 0
    for i in range(1,5+1):
        for j in range(1,9+1):
            if j in range(f,l+1):
                print("* ", end = "")
            else:
                print("  ", end = "")
        f = f - 1
        l = l + 1
        print("\n", end = "")

nine()

def ten():
    print("10.")
    f=1
    l=9
    for i in range(1,5+1):
        for j in range(1,9+1):
            if j in range(f,l+1):
                print("* ", end = "")
            else:
                print("  ", end = "")
        f = f + 1
        l = l - 1
        print("\n", end = "")

ten()

def eleven():
    print("11.")
    mid = int(9/2) + 1
    f=mid
    l=mid
    flag = 0
    for i in range(1,5+1):
        for j in range(1,9+1):
            if j in range(f,l+1):
                if f%2 == 0:
                    if j%2 == 0:
                        print("* ", end = "")
                    else:
                        print("  ", end = "")
                else:
                    if j%2 != 0:
                        print("* ", end = "")
                    else:
                        print("  ", end = "")
            else:
                print("  ", end = "")
        f = f - 1
        l = l + 1
        print("\n", end = "")

eleven()

def twelve():
    print("12.")
    mid = int(9/2) + 1
    f=mid
    l=mid
    flag = 0
    for i in range(1,5+1):
        for j in range(1,9+1):
            if j in range(f,l+1):
                if f%2 == 0:
                    if j%2 == 0:
                        print("* ", end = "")
                    else:
                        print("! ", end = "")
                else:
                    if j%2 != 0:
                        print("* ", end = "")
                    else:
                        print("! ", end = "")
            else:
                print("  ", end = "")
        f = f - 1
        l = l + 1
        print("\n", end = "")

twelve()

def thirteen():
    print("13.")
    mid = int(9/2) + 1
    for i in range(1,9+1):
        if i <= mid:
            for j in range(1,i+1):
                print("* ", end = "")
            print("\n", end = "")
        else:
            for j in range(1,(mid-1)+1):
                print("* ", end = "")
            mid = mid - 1
            print("\n", end = "")

thirteen()

def fourteen():
    print("14.")
    mid = int(9/2) + 1
    for i in range(1,9+1):
        if i <= mid:
            for j in range(1,(mid-i)+1):
                print("  ", end = "")
            for j in range(1,i+1):
                print("* ", end = "")
            print("\n", end = "")
        else:
            for j in range(mid,i):
                print("  ", end = "")
            for j in range(1,(9-i+1)+1):
                print("* ", end = "")
            print("\n", end = "")

fourteen()

def fifteen():
    print("15.")
    mid = 9//2 + 1
    space = 0
    for i in range(mid,1-1,-1):
        for j in range(1,space+1):
            print("  ", end = "")
        space += 2
        for j in range(1,i+1):
            print("* ", end = "")
        print("\n", end = "")
    space -= 4
    for  i in range(mid+1,9+1):
        for j in range(1,space+1):
            print("  ", end = "")
        space -= 2
        for j in range(1,(i-(9//2))+1):
            print("* ", end = "")
        print("\n", end = "")
        
fifteen()

def sixteen():
    print("16.")
    mid = 9//2 + 1
    for i in range(mid,1-1,-1):
        for j in range(1,(i-1)+1):
            print("  ", end = "")
        for j in range(1,i+1):
            print("* ", end = "")
        print("\n", end = "")
    for  i in range(mid+1,9+1):
        for j in range(1,(i-mid)+1):
            print("  ", end = "")
        for j in range(1,(i-(9//2))+1):
            print("* ", end = "")
        print("\n", end = "")
        
sixteen()
