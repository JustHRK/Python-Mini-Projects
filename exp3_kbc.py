Questions = [
    ["What is the capital of France?", "Rome", "Paris", "Berlin", "London", "Paris"],
    ["What is the chemical symbol for water?", "CO2", "NaCl", "H2O", "O2", "H2O"],
    ["Which planet is known as the \"Red Planet\"?", "Venus", "Jupiter", "Saturn", "Mars", "Mars"],
    ["Who wrote the play \"Romeo and Juliet\"?", "Oscar Wilde", "William Shakespeare", "Emily Dickinson", "Jane Austen", "William Shakespeare"],
    ["What is the largest mammal in the world?", "Giraffe", "Elephant", "Blue Whale", "Tiger", "Blue Whale"],
    ["Which country is famous for inventing pizza?", "Spain", "Italy", "India", "China", "Italy"],
    ["What is the tallest mountain in the world?", "Mount Kilimanjaro", "Mount Everest", "Mount McKinley", "Mount Fuji", "Mount Everest"],
    ["What is the chemical symbol for gold?", "Ag", "Fe", "Au", "Hg", "Au"],
    ["Who is the author of the Harry Potter book series?", "Stephen King", "George R.R. Martin", "Agatha Christie", "J.K. Rowling", "J.K. Rowling"],
    ["What is the largest organ in the human body?", "Heart", "Skin", "Liver", "Kidney", "Skin"]
]

def Questioning(lst,i,t):
    amt=(i+1)*1000
    print(f"\n---Question for {amt}$---\n")
    print(f"Q.{i+1}) {lst[0]}")
    print(f"1.{lst[1]}\t\t2.{lst[2]}")
    print(f"3.{lst[3]}\t\t4.{lst[4]}")
    a=int(input("Enter Choice : "))
    if(lst[a]==lst[5]):
        print ("Correct Answer !!!")
        t+=amt
        print (f"Your Total Amount : {t}")
        return t
    else:
        print("Wrong Answer !!!")
        return t
    
#DRiver Code

print("-----Welcome to KBC-----\n")

total=0
i=0
for i in range (10):
    t=Questioning(Questions[i],i,total)
    if(t==total):
        print("\nThat's All for your journey to be a millionaire !")
        print(f"You are Leaving with {total}$")
        break
    else:
        total=t

else:
    print(f"\nCongratulations You are a Millionaire and Won {total}!")