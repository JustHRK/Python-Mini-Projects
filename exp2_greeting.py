t=int(input("Enter time : "))

if(t>=0 and t<24):
    if(t>=5 and t<12):
        print("Good Morning")
    elif(t>=12 and t<17):
        print("Good Afternoon")
    elif(t>=17 and t<21):
        print("Good Evening")
    else:
        print("Good Night")
else:
    print("Invalid Time !")