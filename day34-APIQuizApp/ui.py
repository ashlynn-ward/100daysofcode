#UI Class provides the GUI for the Quiz App

#Import tkinter library and quiz_brain class
from tkinter import *
from quiz_brain import QuizBrain

#Define constants
THEME_COLOUR = "#375362"
FONT = "Arial"

#Create Quiz Interface class
class QuizInterface():

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOUR)

        #Add a label to keep track of score
        self.score_label = Label(text = "Score: 0", fg = "white", bg = THEME_COLOUR, font = (FONT, 15))
        self.score_label.grid(row = 0, column = 1)

        #Create a canvas to display question text
        self.canvas = Canvas(height = 250, width = 300, bg = "white")
        self.q_text = self.canvas.create_text(150, 125, text = "", width = 275, fill = THEME_COLOUR, font = (FONT, 20, "italic"))
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)

        #Add right and wrong buttons
        true_img = PhotoImage(file = "true.png")
        self.true_button = Button(image = true_img, highlightthickness = 0, command = self.true_pressed)
        self.true_button.grid(row = 2, column = 0)
        false_img = PhotoImage(file = "false.png")
        self.false_button = Button(image = false_img, highlightthickness = 0, command = self.false_pressed)
        self.false_button.grid(row = 2, column = 1)

        #Get the first question
        self.get_next_question()

        self.window.mainloop()

    #Methods true_pressed and false_pressed return the user's answer to the quiz brain to determine whether it is right
    def true_pressed(self):
        is_right = self.quiz.check_answer("True", self.quiz.question_list[self.quiz.question_number]["question_answer"])
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    #Method get next question accesses the next question from quiz brain and displays it
    def get_next_question(self):
        self.canvas.config(bg = "white")
        if self.quiz.still_has_questions():
            self.score_label.config(text = f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text = question)
        #Tell user when there are no more questions, and disable the buttons
        else:
            self.canvas.itemconfig(self.q_text, text = "You've completed the quiz!")
            self.true_button.state("disabled")
            self.false_button.state("disabled")

    #Method give_feedback changes the background colour 
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.congig(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_question)


