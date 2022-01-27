# Basics of Python

# While loop and conditions
'''
secret_word = "rojo"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you loose!")
else:
    print("You win!")
'''

# Read an array
'''
office_workers = ["Jim", "Kevin", "Pam", "Dwight"]
for name in office_workers:
    print(name)
'''

# Example of function with parameters and return
'''
def raiseToPower(base_num, pow_num):
    result = 1.0
    for i in range(pow_num):
        result = result * base_num
    return result

base = int(input("Enter base number: "))
pow = int(input("Enter power number: "))

result = raiseToPower(base, pow)

print(result)
'''

# Example of cycle on grid
'''
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for column in row:
        print(column)
'''

# Practice for loops with conditions
'''
def translate(phrase):
    translation = ""

    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    
    return translation

print(translate(input("Enter a phrase: ")))
'''

# Except to specific errors ALWAYS
'''
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as err:
    print(err)
'''

# Reading from a file
'''
employee_file = open("employees.txt", "r")

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
'''

# Writing and appending on files
'''
employee_file = open("index.html", "w")
employee_file.write("<p>This is a paragraph</p>")
employee_file.close()
'''

# Creating and importing a module
'''
import useful_tools-

print(useful_tools.rollDice(6))
'''

# Classes
'''
from Student import Student

var = Student("Rodrigo", "LMAD", 3.1, True)
var2 = Student("Cecy", "LMAD", 2.1, False)

print(var)
'''

# example of class
'''
from Question import Question

question_prompts = [
    "What color are apples?\na) Red/Green\nb) Purple\nc) Orange\n\n",
    "What color are bananas?\na) Teal\nb) Magenta\nc) Yellow\n\n",
    "What color are strawberries\na) Yellow\nb) Red\nc) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def runTest(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got {}/{} correct!".format(str(score), str(len(questions))))

runTest(questions)
'''

# Functions on Objects
'''
from Student import Student

student1 = Student("Rodrigo", "LMAD", 3.1)
student2 = Student("Jarmon", "LA", 3.5)

print(student1.onHonorRoll())
'''

# Herencia
'''
from MexicanChef import MexicanChef

myChef = MexicanChef()
myChef.makeSpecialDish()
myChef.makeTaco()
'''