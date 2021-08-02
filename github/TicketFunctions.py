import zenpy
import creds
import Menus
from zenpy import requests
from zenpy import Zenpy
from colorama import Fore, Style, init
from datetime import datetime

#make sure colorama will work on device
init(convert=True)

#Apply Auth info
auth = { "email":creds.emailA, "token":creds.tok, "subdomain":creds.domain}
zenpy_client = Zenpy(**auth)

#view a single ticket
def viewSingle(tId):
    try:
        ticket = None

        #Gets single ticket by id from api
        ticket = zenpy_client.tickets(id = tId)

        #Print ticket info
        if ticket != None:
            time = datetime.strptime(str(ticket.created_at), "%Y-%m-%dT%H:%M:%SZ")
            print(Fore.CYAN + ("Ticket with ID " + str(ticket.id)).center(100) + "\n" + ("Submitted by " + str(ticket.submitter_id) + " on " + time.strftime("%a %b %d %Y at %I:%M %p")).center(100) + "\n" + ("Ticket Status: " + str(ticket.status)).center(100) + "\n" + ("Assigned to: " + str(ticket.assignee_id)).center(100) + "\n" + ("Subject: " + str(ticket.subject)).center(100) + "\n" + ("Description: " + str(ticket.description)))
            return Menus.returnToTicketMenu()

        #If ticket exeption not thrown and ticket not found throw a program error
        else:
            print("There was a program error.\nReturning to ticket menu")
            return(True)


    except zenpy.lib.exception.RecordNotFoundException:
        print("Unable to find ticket id. Make sure you are entering a valid ticket id number.\nReturning to ticket menu")
        return(True)


    except zenpy.lib.exception.APIException:
        print("There was an API error, please check that that the cred information is correct. This error can also be thrown if you type a string instead of a ticket id number")
        return(True)

    except requests.exceptions.ConnectionError:
        print("There was a problem connecting to the API. Please check your internet connection.")
        return(True)


#View all tickets
def viewAll():
    try:
        count = 0
        ticketObj = zenpy_client.tickets()
        ticketGen = ticketObj[::]
        gLen = len(ticketGen)

        #If there is at least one avialable ticket in the account then start the first page
        if gLen != 0:
            pages = True
            ticketPage = ticketGen[0:25]
            pCount, i, j = 1, 0, 25

        else:
            pages = False

        while pages:
            count += 25
            print(Fore.CYAN + ("Showing Page " + str(pCount)).center(100) + "\n")

            #prints all tickets on a page
            for ticket in ticketPage:
                time = datetime.strptime(str(ticket.created_at), "%Y-%m-%dT%H:%M:%SZ")
                print(Fore.CYAN + "Ticket with id: " + str(ticket.id) + "|Assigned to: " + str(ticket.assignee_id) + "|created on " + time.strftime("%a %b %d %Y at %I:%M %p") + "|Ticket Subject: " + str(ticket.subject))

            #Ask for a new page if there are still tickets available
            if count < gLen:
                if Menus.askPage() == False:
                    i += 25
                    j += 25
                    ticketPage = ticketGen[i:j]
                    pCount +=1

                #returns to main menu if user does not go to next page
                else:
                    pages = False
                    return True

            #Display when no more tickets are avaialable and exit pages
            else:
                print("No more tickets available to be displayed.")
                pages = False

        #If there are no tickets in the user account
        if count == 0:
            print("No Tickets Available at this time. Please add tickets to your zendesk account in order to view them")

        return Menus.returnToTicketMenu()

    except zenpy.lib.exception.APIException:
        print("There was an API error, please check that that the creds information is correct.")
        return True

    except requests.exceptions.ConnectionError:
        print("There was a problem connecting to the API. Please check your internet connection.")
        return True