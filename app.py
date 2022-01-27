# Basics of Python

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

'''
office_workers = ["Jim", "Kevin", "Pam", "Dwight"]
for name in office_workers:
    print(name)
'''

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

