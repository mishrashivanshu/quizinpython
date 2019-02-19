print('Who was the first Prime Minister of Democratic India ?\n', 'a.)\tNarendra Modi\n', 'b.)\tPandit Jawahar Lal Nehru\n', 'c.)\tSmt. Indira Gandhi\n', 'd.)\tMahatma Gandhi')
answer = input("Enter Your Answer:")
if answer =='b':
    print("Yes you are correct my Brother!")
else:
    print('Sorry, But you are wrong')
if answer=='b':
    Earned_Points= +4
else:
    Earned_Points= -1
print('You Have Earned:', Earned_Points, 'Points')
answer = input("Do You Want to Have Some More Fun With GK ?")
if answer=='y':
    print("Which one of the following was one of the cofounders of Microsoft Corporation ?\n", "a.)\tPaul Allen\n", "b.)\tWilliam Shockley\n", "c.)\tSteve Jobs\n", "d.)\tSteve Wozniak")
    answer= input("Enter Your Answer:")
    if answer=='a':
        print("Yes you are correct my Brother!")
    else:
        print('Sorry, But you are wrong')
    if answer=='a':
        Earned_Points= +4
    else:
        Earned_Points= -1
    print('You Have Earned:', Earned_Points, 'Points')
    answer= input("Press 'n' for next question or 'q' for ending the quiz. ")
    if answer== 'n':
        print("Who was the inventor of WhatsApp ?\n", "a.)\tJane Koum\n", "b.)\tMark Zukerberg\n", "c.)\tBill Gates\n", "d.)\tYOU")
        answer= input("Enter Your Answer:")
        if answer=='a':
            print("Congo! You are Correct.")
            print("You have in your pocket 4 points.")
        else:
            print("Sorry! But you are wrong.")
            print("You have -1 points in your pocket.")
        answer= input("Do you want to play more?")
        if answer== 'y':
            print("How many alphabets are there in English Language ?\n", "a.)\t26\n", "b.)\t32\n", "c.)\t12\n", "d.)\t10\n")
            answer= input("Enter Your Answer:")
            if answer=='a':
                print("Good, You are correct.")
                print("Earned Points= 4")
            else:
                print("Sorry, But Wrong Answer.")
                print("You earned -1 points for this question.")
            answer= input("Are you enjoying the quiz ? Press 'y' for yes and 'n' for no")
            if answer=='y':
                answer= input("Should I throw the next question?")
                if answer== 'y':
                    print("Which Ved of the following is newest?\n", "a.)\tRigveda\n", "b.)\tSamaveda\n", "c.)\tYajurveda\n", "d.)\tAtharveda")
                    answer= input("Enter Your Answer:")
                    if answer=='a':
                        print("Correct! You have an insight of Vedas.")
                        print("Congo! You Earned 4 points.")
                    else:
                        print("Sorry You got it wrong. Along with the knowledge of the technology imported from west we should\nposess an insight of our own rituals and texts.")
                        print("You earned -1 points for this question.")
                print("So here we mark the end.\nI really had a great time in programming this quiz. Thanks to Mr. AAKASH GOEL FOR THIS BBEAUTIFUL TASK.\nRegards,\nSHIVANSHU MISHRA,\nBTECH I YEAR, CSE\n KIET GROUP OF INSTITUTIONS")
            else:
                print("Feel Free to close the quiz window anytime!")
        else:
            print("OKAY! See you soon close the quiz window.")
    elif answer== 'q':
        print("You are free to close the quiz.")
else:
    print("OKAY! You are free to leave... See You Soon... I will miss you")