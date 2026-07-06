while True:
    print("welocome to the pattern generator and number analyzer...!")
    print("select an option:")
    print("1. right angle triangle")
    print("2. pyramid")
    print("3. left-angled triangle")
    print("4. analyze a range of numbers")
    print("5. exit")

    choice=int(input("enter your choice : "))

    if choice==1:
        rows=int(input("enter the number of rows : "))
        if rows<=0:
            print("invalid rows...!")

        print("right angled pyramid")
        for i in range(1,rows+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()   

    elif choice==2:
        print("yoy enter 2")

        rows=int(input("enter the number of rows"))
        if rows<=0:
            print("invalid rows...!")
        print("pyramid pattern")
        for i in range(rows):
            for space in range(rows-i-1):
                print(" ",end=" ")
            for j in range(2*i+1):
                print("*",end=" ")
            print()    
                
    elif choice==3:
        print("you enter 3")
        rows=int(input("enter the number of rows"))
        if rows<=0:
            print("invalid rows")
        print("left angle triangle")
        for i in range(1,rows+1):
            for space in range(rows-i+1):
                print(" ",end=" ")
            for j in range(i):
                print("*",end=" ")
            print()        

    elif choice==4:
        print("you enter 4")

        start=int(input("enter the starting number"))
        end=int(input("enter the ending number"))
        if end<start:
            print("end number must be greater then start number")
            continue
            
        total=0
        for i in range(start,end+1):
            if i==0:
                pass
            elif i%2==0:
                print(f"number{i} is even")
            else:
                print(f"number{i} is odd")   

    elif choice==5:
            print("you enter 5")
            print("Thank you")
    else:
            print("invalid chioce")   
            break