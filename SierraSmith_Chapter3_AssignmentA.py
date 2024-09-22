# Expense Tracker Program
# Prompts the user for a list of their expenses, then calculates and displays the
# highest expense, lowest expense, and total of all expenses


import functools
import time

# dividers for neater code
DIV = "---" * 30


def delay():


    time.sleep(.7)


def expense_tracker():


    initial()


def initial():


    # one-time welcome message displayed when program starts
    print("\nHello! Welcome to the nation's most trusted Expense Tracker.")
    print(DIV)

    run()


def run():

    # example input defined and displayed before "info" prompt
    EXAMPLE = "For example: computer 1200; electric 252.89; gas 100.75\n"

    # directions for user
    print("Please list the names and amounts of your monthly expenses.\n")
    print(EXAMPLE)

    # user input saved to "info" variable
    info = input("")
    print('\n')

    check(info)


def check(info):


    # checks for semicolons in "info" string
    if ';' not in info:

        # displays user input with a prompt to retry
        print(f"Your input: {info}")
        print("Oops! You forgot to insert a semicolon somewhere.\n")

        # prompt reiterates until user enters input correctly
        while ';' not in info:
            print("Please reenter the expense names and amounts correctly :)\n")

            info = input("")

    # when "info" is inputted correctly, list_maker() iterates
    list_maker(info)


def list_maker(info):


    # splits "info" into separate expenses
    expenses = info.split(";")

    # print(f"Expenses split into one list: {expenses}")

    # empty list where all expenses will be stored
    new = []

    # empty list where all numerical data will be appended and calculated
    nums = []

    # for each item in "expenses", reformat:
    # -strip off all leading and following whitespace -capitalize first letters
    # -split item into a sub list -assign each reformatted item to "n" and
    #  append it to "new"
    for i in expenses:

        n = i.strip().capitalize().split()

        new.append(n)

    # print(f"Complete list of expenses: {new}")

    # grab the value in the last index of each sub list and append it to "nums"
    # - each expense amount from "new" gets assigned to "num," reformatted as a float
    #   and appended to "nums"
    for i in new:

        num = float(i[-1])

        nums.append(num)

    # print(f"All numbers from expense list: {nums}")

    analyze(new, nums)


def analyze(new, nums):


    # lambda function; adds all numbers in "nums" together, saves the result to "total"
    total = functools.reduce(lambda a, b: a + b, nums)


    # lambda function; compares all numbers in "nums," saves the highest number to "highest"
    highest = functools.reduce(lambda a, b: a if a > b else b, nums)

    # find the index of "highest" number in "nums", save the result to "high_index"
    high_index = nums.index(highest)

    # use "high_index" to grab the corresponding expense name and amount from "new" list
    # the [0] and [1] index of that expense is organized as [name, amount],
    # therefore, specifying those indexes will result in grabbing the right expense name and amount
    high_label = new[high_index][0]
    high_amount = new[high_index][1]


    # lambda function; compares all numbers in "nums," saves the lowest number to "lowest"
    lowest = functools.reduce(lambda a, b: a if a < b else b, nums)

    # find the index of "lowest" number in "nums," save the result to "low_index"
    low_index = nums.index(lowest)

    # use "low_index" to grab the corresponding expense name and amount from "new" list
    low_label = new[low_index][0]
    low_amount = new[low_index][1]


    # (optional) counts how many items are in "nums" list and assigns number to "items"
    # items = len(nums)

    print(DIV)

    # (optional) displays how many "items" were calculated in final summary
    # print(f"Summary of All {items} Expenses")

    # final summary message
    print("Summary of Expenses")

    print(DIV)

    # displays all final amounts and expense labels
    print(f"Total: ${total}"
          f"\nHighest expense: {high_label}, ${high_amount}"
          f"\nLowest expense: {low_label}, ${low_amount}")

    restart()


def restart():


    print(DIV)

    delay()

    # prompts user for input to continue or end program
    again = input("Enter y to start a new calculation or n to quit: ")

    # if user entered y, program loops back to run()
    if again == "y" or again == "Y":

        # confirmation restart message
        print("\nPreparing for new calculation...")
        print(DIV)
        delay()

        run()

    # ends program if user didn't enter y
    else:

        print(DIV)

        # final message
        print("Thank you for choosing Expense Calculator!")
        time.sleep(4)


# call to start program
expense_tracker()