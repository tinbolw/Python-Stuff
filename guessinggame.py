
secret_word = "Volvo"
guess = ""
guesses = 0
guess_limit = 10
out_of_guesses = False
x = 9


while guess != secret_word and not(out_of_guesses):
    if guesses < guess_limit:
        guess = input("Enter Guess: ")
        print("You have " + str(x) + " guesses remaining")
        guesses += 1
        x -= 1
    else:
        out_of_guesses = True

if out_of_guesses == True:
    print("You lost.")
else:
    print("You Win!")
















