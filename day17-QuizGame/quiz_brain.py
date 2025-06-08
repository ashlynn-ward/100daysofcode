#Clas Quiz Brain kep track of what question the user is on and stores the questions
class QuizBrain():
    def __init__(self, q_list):
        self.question_number =0
        self.question_list = q_list
        self.score = 0
    
    #Method next_question retrieves the next question in the list, displays it, and prompts user to answer it
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer= input(f"Q.{self.question_number}: {current_question.text}. True/False:")
        #Validate user input
        while user_answer!="True" and user_answer!="False":
            user_answer = input("Invalid input. Enter True/False:")
        self.check_answer(user_answer, current_question.answer)

    #Method still_has_questions checks whether there are still questions in the bank and returns a boolean
    def still_has_questions(self):
        return self.question_number<len(self.question_list)
 
    #Method check_answer checks whether the user has chosen the correct answer and displays the score
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score+=1
            print("You got it right!")
        else:
            print(f"Sorry, the correct answer was {correct_answer}.")

        print(f"Current score: {self.score}/{self.question_number}\n\n")