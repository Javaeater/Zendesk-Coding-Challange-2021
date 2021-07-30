import Menus
import TicketFunctions
from colorama import Fore, Back, Style
from colorama import init

#main function
if __name__ == '__main__':

    print(f"{'Zendesk Ticket Viewer version 1.0.0' : ^100}")
    run = Menus.startTicketView()

    while run:
        ans = Menus.displayMenu()
        if ans.lower() == 'view':
            idSelect = input("What ticket would you like to view?\n")
            run = (TicketFunctions.viewSingle(idSelect))
        elif ans.lower() == 'view all':
            run = TicketFunctions.viewAll()
        elif ans.lower() == "qt":
            run = False
        else:
            print("Invalid entry. Please refer to the menu for ticket options")

    print("Thank you for using the Zendesk Ticket Viewer")