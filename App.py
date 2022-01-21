# --------------------- CLASSES & OBJECTS -----------------

# CLASSES are a datatype that we can use when strings, integers, and bolleans aren't sufficient
# to use a class we created a SEPARATE file named after the class: student.py

# CLASS - definition or specification of what the object is made of
# OBJECT - the actual object


print("--------------------Classes Example 1--------------------")

from Student import Student
# ^ from this file      ^ import this class

student1 = Student("Simba", "Accounting", 3.1, False)
#   ^ we're creating a student ^ and passing in the student's info/values
student2 = Student("Charlie", "Criminal Law", 2.0, True)

print(student1.name)
#       ^ pass in the student and ask for specific info/value we want returned
print(student1.gpa)
print(student1.major)
print(student1.is_on_probation)


print("--------------------Classes Example 2--------------------")

from Student import Student
# ^ from this file      ^ import this class

student1 = Student("Simba", "Accounting", 3.1, False)
#   ^ we're creating a student ^ and passing in the student's info/values
# this info gets sorted by the INITIALIZE function in our CLASS and connects whatever we submitted
# as the

print(student1.name)
#       ^ pass in the student and ask for specific info/value we want returned
print(student1.gpa)
print(student1.major)
print(student1.is_on_probation)


print("--------------------Building a Quiz --------------------")

'''
from Question import Question

question_prompts = [
    "What color are maracuya?\n(a) Yellow\n(b) Purple\n(c) Orange\n\n",
    "What color are mangoes?\n(a) Green/Red\n(b) Yellow\n(c) Pink\n\n",
    "What color are bananas?\n(a) Yellow\n(b) Green\n(c) Orange\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a")
]
# these are the correct answers for the quiz questions


def run_test(questions):
    score = 0
    # this for loop will run through the questions and increase the score when the response matches our 'correct answers'
    for question in  questions:
    # for each question in the questions array I want to do something
        answer = input(question.prompt)
        # ^ user response/input stored in this variable
        if answer == question.answer:
        # checking is response/input matches our 'correct answers'
            score += 1
            # here we'll be increasing the score when correct
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    # integer to string ^ converter             ^ number in questionaire finder so no matter how many questions we add it'll increase

run_test(questions)
'''

print("--------------------Object Functions Example 1--------------------")

from Customer import Customer

Customer1 = Customer("Simba", 2, 150)
Customer2 = Customer("Charlie", 6, 20)

print(Customer1.got_reward_points())
print(Customer2.got_reward_points())

# a class function is a function used by objects in that class



print("--------------------Inheritance Example 1--------------------")

# Inheritance, where a new Class can inherit the attributes of a dif Class

from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChineseChef = ChineseChef()


myChef.make_salad()
# the chef class works
myChineseChef.make_friedRice()
# the chinese chef class function works

myChineseChef.make_chicken()
# here we see that the chinese chef class can access the functions from the chef file
myChineseChef.make_special()
# because of the over ride function in the chinese chef file, this function won't return the inherited chef files definition of the function

# --------------------PYTHON INTERPRETER--------------------
# terminal > python3 *enter* = python interpreter