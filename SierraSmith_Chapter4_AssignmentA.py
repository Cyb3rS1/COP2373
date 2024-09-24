# Spam Email Detective Agency

# This program takes an email message entered by the user and tests the likelihood of the
# email being spam based on a list of words/phrases commonly used in spam emails.
# For each spam word/phrase detected, a spam score accumulates.
# The program outputs the spam score and all the words/phrases that impacted the score.


# module imported for sleep() function
import time

# (1) make_timer function; records how long this file runs
def make_timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret_val = func(*args, **kwargs)
        t2 = time.time()
        print('Time elapsed was', t2 - t1)
        return ret_val
    return wrapper

# (2) count_nums function that fills make_timer function param
@make_timer
def count_nums(n):
    for i in range(n):
        for j in range(1000):
            pass

# (3) variable containing make_timer function that passes count_nums as a param
count_nums = make_timer(count_nums)


# global variable: divider for code organization
DIV = "__" * 30


# main function where every other function resides
def seda():


    # beginning greeting
    print("Hello! Welcome to your local Spam Email Detective Agency; SEDA for short.")

    print(DIV)


    process()


# first function in seda(); carries out entire operation of taking user input, scanning
# the input for spam words, processing scores and percentages, and printing out the results
def process():


    # word bank of words and phrases commonly found in spam emails
    spam_words = ["free", "best price", "no cost", "fast cash", "earn",
                  "free gift", "guaranteed", "incredible deal", "secure", "risk-free",
                  "save up to", "act now", "apply", "click here", "don't wait",
                  "exclusive", "instantly", "now", "while supplies last", "winner",
                  "no interest", "bonus", "offer", "urgent", "save big",
                  "save $$$", "limited-time", "don't delete", "refinance", "you've been selected"]

    # spam score that will accumulate with each spam word/phrase found in user input
    spam_score = 0

    # where user input gets recorded, followed by a .lower() method. The .lower() method enables all
    # instances of spam words/phrases found in the email variable to be matched with items in spam_words
    # regardless of their initial lettercase.
    email = input("Enter the suspicious email here: \n").lower()

    # counts how many words are in email
    word_count = len(email.split())

    # displays word_count
    print(f"Word count: {word_count}")

    print("\n")


    # time.sleep() acts as a little delay for the "scanning" process
    time.sleep(.5)

    print("Scanning for suspicious words...")

    time.sleep(2)

    # for loop that goes through every index of spam_words
    for word in spam_words:


        # compares the indexed word from spam_words to email variable
        if word in email:

            # counts how many occurrences of "word" are in spam_words list
            x = email.count(word)

            # adds number of occurrences to the ongoing spam score
            spam_score += email.count(word)

            # capitalizes first letter of matched word or phrase from spam_words
            current_word = word.capitalize()


            # conditional statement that adds specificity to output :)
            if x > 1:

                print(f'"{current_word}" was found {x} times.')
                time.sleep(.7)

            else:
                print(f'"{current_word}" was found {x} time.')
                time.sleep(.7)


    # spam_score reformatted into a percentage
    ss_per = round(spam_score / 30 * 100)

    # percentage of how many spam words make up the email's entirety
    part = round(spam_score / word_count * 100)

    print(f"\n")

    # statement displayed for each successful scan
    print(f"Email scanning complete.")

    print(DIV)

    # empty variable that will be assigned in the following statement
    rate = ""


    # conditional statement that assigns rate variable based on part and ss_per comparison

    if part >= ss_per:

        if part <= 10:
                rate = "isn't"

        if 10 < part < 25:
                rate = "is less"

        if 25 < part < 50:
                rate = "is somewhat"

        if 50 < part < 75:
                rate = "is very"

        if 75 < part <= 100:
                rate = "is extremely"

    elif part < ss_per:

        if ss_per <= 10:
            rate = "isn't"

        if 10 < ss_per < 25:
            rate = "is less"

        if 25 < ss_per < 50:
            rate = "is somewhat"

        if 50 < ss_per < 75:
            rate = "is very"

        if 75 < ss_per <= 100:
            rate = "is extremely"


    # conditional statement determines which result statement will be printed
    if spam_score == 0:
        print("No spam words detected.")

    elif spam_score >= 1:
        # saves end result to a variable (includes original and reformatted spam_score, part
        # percentage, and final rating.)
        result = str(f"Spam score: {spam_score} out of 30 points ({ss_per}%).\n"
                    f"{part}% of the email contained spam words.\n"
                    f"Based on these calculations... This email {rate} likely to be spam.")

        # displays result
        print(result)

    print(DIV)

    again()


# last function to iterate in seda(); restarts process() function or terminates loop
# based on user input
def again():

    # preset variable that enables the following prompt to iterate
    yes = "y"

    print("Scan another email?")

    # variable changes or stays the same based on user input
    yes = input("Enter y for yes or other key to exit: ")

    print(DIV)

    # determining loop that reiterates process() function or stops the program.
    # if user enters Y or y, the user gets taken back to process() function
    # where they can enter a new email to be scanned
    if yes == "y" or yes == "Y":

        process()
    else:

        # iterates when user presses any other key besides y; terminating statement
        print("Thank you for visiting the Spam Email Detective Agency.")


# call to start the main function
seda()

# (4) call to record and display the program's run-time
count_nums(33000)