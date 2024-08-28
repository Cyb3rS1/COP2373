# Movie ticket purchase portal
# A program that acts as a platform for buying movie tickets


# global variables for:

MAX_TICKETS = 4     # max tickets per person (constant)
tickets_left = 20   # starting total of remaining tickets
buyers = 0          # accumulator total number of buyers


# first function in ticket_portal: starting point of each transaction
def greeting():

    print("====================================")
    print("Hello and welcome to the cinema!")
    print("How many tickets would you like to buy? Disclaimer: Max 4 per person.")
    num = int(input("Please enter a numeric digit: "))

    # next function that prompts user if input is invalid
    input_invalid(num)


# second function in ticket_portal: tests for valid input
def input_invalid(num):


    if num > MAX_TICKETS or num <= 0:
        print("You may only purchase up to 4 tickets.")
        print("====================================")

        while num > MAX_TICKETS or num <= 0:
            # ensures valid input (number between 1 and 4)
            num = int(input("Please enter a valid number: "))

    # following function that prompts user if they requested more tickets
    # than there are available
    check_tickets_left(num)


# third function in ticket_portal: checks how many tickets are available
def check_tickets_left(num):

    global tickets_left

    if num > tickets_left:

        if abs(tickets_left) == 1:
            print(f"Unfortunately, there is only {abs(tickets_left)} ticket left.")

        else:
            print(f"Unfortunately, there are only {abs(tickets_left)} tickets left.")

        while num > tickets_left:
            # ensures valid input (num < tickets_left)
            num = int(input("Please enter a number accordingly: "))

    # following function that informs user of a successful purchase
    purchase_successful(num)


# forth function in ticket_portal: where every purchase is confirmed
def purchase_successful(num):

    global tickets_left
    global buyers

    # deducts number of tickets purchased from limited total
    tickets_left -= num

    # accumulates by 1 for each transaction
    buyers += 1

    # message of transaction completion and remaining tickets
    print("====================================")
    print("Purchase successful! Thank you and enjoy the show.")

    if tickets_left == 1:
        print(f"There is {tickets_left} ticket left.")

    else:
        print(f"(There are {tickets_left} tickets left.)")


# last function in ticket_portal: iterates when tickets are sold out
def end_loop():

    global buyers

    # end of entire function message and total number of buyers
    print("====================================")
    print("Sorry folks, this showing is sold out.")
    print(f"There were {buyers} buyers today.")



# main function containing all other functions and a condition for them to work:
# where the beginning and end of each purchase transaction occurs
def ticket_portal():

    # reference to global variables
    global tickets_left
    global buyers

    # condition required for ticket transactions to occur
    while tickets_left > 0:

        # main loop where nested conditional loops interact
        greeting()

    # ending statements of the loop when all tickets have been sold
    end_loop()


# begin ticket purchase portal
ticket_portal()