
from colorama import Fore, Style, init
init(convert=True)

#First start menu
def startTicketView():
    start = False

    while start == False:
        o1 = input("Type 'op' to view the Ticket options menu or 'qt' to exit.\n")

        if o1.lower() == 'op' :
            start = True
            run = True

        elif o1.lower() == "qt" :
            start = True
            run = False

        else:
            print("Invalid input please select from one of these options:")
    return (run)

#Ask user to return to ticket menu
def returnToTicketMenu():
    print(Fore.RESET)
    tikM = input( "Would you like to return to the Ticket Menu? Type 'y' to continue to the menu or type 'qt' to exit the program.\n")

    if tikM.lower() == 'y':
        run = True

    elif tikM.lower() == 'qt':
        run = False

    else:
        print("Invalid option. Automatically returning to ticket menu.")
        run = True
    return run

#display the main menu
def displayMenu():
    menT = (Fore.YELLOW + 'Ticket Menu')
    print(Fore.YELLOW + menT.center(100, "_"))
    print("-- Type 'view' to see in depth information on a single ticket --".center(100))
    print("-- Type 'view all' to see a basic overview of all tickets --".center(96))
    print("-- Type 'qt' to quit the program --".center(71))
    menuSelect = input()
    return(menuSelect)

def askPage():
    print(Fore.GREEN)
    nP = input(
        "Would you like to view the next page of tickets? Type 'y' to view the next page of tickets or 'tm' to go to the ticket menu.\n")
    if nP.lower() == 'y':
        return False

    elif nP.lower() == 'tm':
        return True

    else:
        print("Invalid option. Automattically returning to ticket menu.")
        return True
