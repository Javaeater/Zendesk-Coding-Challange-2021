import Menus
import TicketFunctions
import pyfiglet
from colorama import Fore, Style, init

#make sure colorama will work on device
init(convert=True)

#main function
if __name__ == '__main__':

    #Print ascii start banner
    startBanner = pyfiglet.figlet_format("Zendesk Tickets")
    print(Fore.CYAN + startBanner)
    run = Menus.startTicketView()

    #run the program while true
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