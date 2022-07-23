print("Welcome to my computer quiz!!")
a=input("So are you ready? "
        "Type Yes or No")
if a=='no' or a=='No':
    quit()
elif a=='yes' or a=='Yes':
    print("So lets Play")
else:
    print("Wrong Input")
your_score=0
Wrong_answer=0
answer= input("What is full form of CPU? ")
if answer=="Central Processing Unit" or answer=="central processing unit":
    print("Congrats Your answer is correct")
    your_score +=1

    print("Your Score is ",your_score)
    print("Wrong Answers= ",Wrong_answer)
else:
    print("Wrong answer")

    Wrong_answer +=1
    print("Your Score is ",your_score)
    print("Wrong Answers= ",Wrong_answer)
answer= input("What is full form of GPU? ")
if answer=="Graphic Processing Unit" or answer=="graphic processing unit":
    print("Congrats Your answer is correct")
    your_score +=1

    print("Your Score is ",your_score)
    print("Wrong Answers= ",Wrong_answer)
else:
    print("Wrong answer")

    Wrong_answer += 1
    print("Your Score is ",your_score)
    print("Wrong Answers= ",Wrong_answer)
answer= input("What is full form of RAM? ")
if answer=="Random Access Memory" or answer=="random access memory":
    print("Congrats Your answer is correct")
    your_score += 1

    print("Your Score is ",your_score)
    print("Wrong Answers= ",Wrong_answer)
else:
    print("Wrong answer")

    Wrong_answer += 1
    print("Your Score is ",your_score)
    print("Wrong Answers= ",Wrong_answer)
answer= input("What is full form of ROM? ")
if answer=="Read Only Memory" or answer=="read only memory":
    print("Congrats Your answer is correct")
    your_score += 1

    print("Your Score is ",your_score)
    print("Wrong Answers= ",Wrong_answer)
else:
    print("Wrong answer")

    Wrong_answer += 1
    print("Final Score is ",your_score)
    print("Final Wrong Answers= ",Wrong_answer)