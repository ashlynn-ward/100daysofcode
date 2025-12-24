#API Quiz App
#Ashlynn Ward, June 13, 2025
#This program uses classes from  Day 17: Quiz Game. However, it draws its questions from an API request

#Import Question, question_data, QuizBrain, and UI 
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

#Import os library
import os

#Change working directory so program can access files
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

#Add questions to bank
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#Create quiz using quiz brain, and show ui
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

#Print final score
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
