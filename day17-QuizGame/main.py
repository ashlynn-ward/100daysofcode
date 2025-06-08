#Import related files
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#Define a list to store questions
question_bank=[]

#Add each item in question_data to question_bank as a Question object
for question in question_data:
    q = Question(question["text"], question["answer"])
    question_bank.append(q)

#Create quiz
quiz = QuizBrain(question_bank)

#While there are still questions, continue to ask the next question
while quiz.still_has_questions():
    quiz.next_question()

#Print the final score 
print(f"You've completed the quiz! Your final score: {quiz.score}/{quiz.question_number}")