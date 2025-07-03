import time

qna = [{"question":"What is the color of an apple?",
        "options":["Red", "Blue", "Yellow"], "corr_option":"Red"},
       {"question":"Which of the following is an animal?",
        "options":["Spider", "Ant", "Zebra"], "corr_option":"Zebra"},
       {"question":"Is the sun a star?",
        "options":["True", "False"], "corr_option":"True"}]

def play():
    score = 0
    for i in range(len(qna)):
        index = qna[i]
        print(str(i + 1) + ") " + index["question"])
        
        for j in range(len(index["options"])):
            print("   (" + str(j + 1) + ") " + index["options"][j])
                           
        ans = input("Ans: ")
        
        print("\n")
        if ans.upper() == index["corr_option"].upper():
            score += 1
    print("Calculating...")
    time.sleep(2)
    print(f"You got {score}/{len(qna)}")
                           
want_to_play = input("Do you want to play?(y/n)\n")

if want_to_play.upper() == "Y":
    play()
else:
    print("Ok then, Bye. :'C")
