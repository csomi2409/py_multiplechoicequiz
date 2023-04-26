from question_class import Question             #Import the class from the module

#Self customizable list. Try putting in an another question with answers
question_prompt = [
    "What color is an apple?\n(A)Red\n(B)Blue\n(C)Brown\n\n",
    "What color is a Ferrari?\n(A)Brown\n(B)Purple\n(C)Red\n\n"
]

#If you've added a question to 'question_prompt' make sure to add the index and the CORRECT answer here
Questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c")
]

def test(Questions):                                    #A function to test the user's input
    points = 0                                          #Points that you can earn by getting the answers right 
    for i in Questions:                                 #For loop to test each question
        answer = input(i.question).lower()              #Ask for an input and convert it into lowercase
        if answer == i.answer:                          #If the answer is correct
            points += 1                                 #Add 1 to your points
    print("Thanks for playing!\nYou've got " + str(points) + " out of " + str(len(Questions)) + " right!")

#Call the function
test(Questions)