a=int(input("Enter Number A :"))
b=int(input("Enter Number B :"))
while(True):
    print("""Choose Operation:
        1.Addition
        2.Sutraction
        3.Multiplication
        4.Division
        5.Exit\n""")

    ch=int(input("Enter Choice : "))
    print()
    if(ch==1):
        print("A + B = ",a+b)
    elif(ch==2):
        print("A - B = ",a-b )
    elif(ch==3):
        print("A * B = ",a*b)
    elif(ch==4):
        print("A / B = ",a/b)
    elif(ch==5):
        print("Program Closed")
        break
