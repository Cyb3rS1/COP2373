# Magic 8-ball: This program acts as a digital magic 8-ball that gives you a randomly
# generated answer every time you shake it, just like the real deal! The program creates a
# text file and populates it with possible replies from the 8-ball, then picks and displays
# a random reply to answer the user's question. This whole iteration continues until the
# user enters "q" signaling that they got bored with the 8-ball.

# imported module needed for suspenseful delay
import time

# imported module needed for randomized choice
import random


# used to divide parts of the output dialogue
DIVIDER = "-" * 30

# 1st function to execute in magic8ball()
# creates a txt doc with magic 8-ball answers,
# stores each answer into a list, generates a random answer
def generate_answer():

    # empty list where each "answer" from the doc will be stored
    options = []

    # creates and opens new doc for populating with 8-ball answers
    answers = open("8ball_responses.txt", "w")

    # writes text to file delimited by \n
    answers.write("Yes, of course!\nWithout a doubt, yes.\nYou can count on it."
                  "\nFor sure!\nAsk me later\nI'm not sure."
                  "\nI can't tell you right now.\nI'll tell you after my nap."
                  "\nNo way!\nI don't think so.\nWithout a doubt, no."
                  "\nThe answer is clearly NO!")


    # file is closed for writing
    answers.close()

    # file is opened for reading
    answers = open("8ball_responses.txt", "r")

    # file's read contents are saved to "data" object
    data = answers.read()

    # the contents in "data" are separated by \n delimiter and
    # stored in "options" (empty list)
    options = data.split("\n")

    # "answer" variable is assigned to a random choice from "options"
    answer = random.choice(options)

    # "answer" gets passed on to q_and_a
    q_and_a(answer)


# 2nd function to execute in magic8ball()
# where the user asks a question and receives a randomized
# answer from magic 8-ball responses
def q_and_a(answer):

    input("Ask it a yes or no question: ")

    print("You shake the magic 8-ball...")

    # simulates a suspenseful delay
    time.sleep(3)

    # outputs "answer" passed from q_and_a() function
    print(f'The magic 8-ball says, "{answer}"')

    # continues to conditional "continue or end" statement
    replay_or_end()


# 3rd (last) function to execute in magic8ball()
# prompts user for input, conditional statement
# determines if magic8ball() loop will reiterate or end
def replay_or_end():

    print(DIVIDER)

    # determining input variable
    again = input(f"Try again? \nPress any key + enter to continue or q to quit: ")

    # conditional statement depending on user input
    if again != "q" and again != "Q":
        generate_answer()

    # signals end-of-game
    else:
        print("You got bored of the 8-ball.")


# main function that contains "the game flow" (every other function)
def magic8ball():

    # beginning greeting
    print("Try your luck with the all-knowing magic 8-ball! \nWatch as it"
          " reveals your fate!")
    print(DIVIDER)

    # "game flow" initiating function
    generate_answer()



# call the main function
magic8ball()