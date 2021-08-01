import zenpy
import creds
import Menus
from zenpy import requests
from zenpy import Zenpy
from colorama import Fore, Style, init
from datetime import datetime

init(convert=True)
auth = { "email":creds.emailA, "token":creds.tok, "subdomain":creds.passWd}
zenpy_client = Zenpy(**auth)

#view a single ticket
def viewSingle(id):
    try:
        tk = None
        #Finds the matching ticket in search if available
        for ticket in zenpy_client.search(type='ticket', query=id):
            tk = ticket

        #Print ticket info
        if tk != None and str(ticket.id) == id:
            time = datetime.strptime(str(ticket.created_at), "%Y-%m-%dT%H:%M:%SZ")
            print(Fore.CYAN + ("Ticket with ID " + str(ticket.id)).center(100) + "\n" + ("Submitted by " + str(ticket.submitter_id) + " on " + time.strftime("%a %b %d %Y at %I:%M %p")).center(100) + "\n" + ("Ticket Status: " + str(ticket.status)).center(100) + "\n" + ("Assigned to: " + str(ticket.assignee_id)).center(100) + "\n" + ("Subject: " + str(ticket.subject)).center(100) + "\n" + ("Description: " + str(ticket.description)))
            return Menus.returnToTicketMenu()

        #If ticket not found retun to ticket menu
        else:
            print("Unable to find ticket id. Make sure you are entering a valid ticket id.\nReturning to ticket menu")
            return(True)


    except zenpy.lib.exception.APIException:
        print("There was an API error, please check that that the API token is correct")
        return(True)


    except requests.exceptions.ConnectionError:
        print("There was a problem connecting to the API. Please check your internet connection.")
        return(True)


#View all tickets
def viewAll():
    try:
        count = 0
        pCount = 1
        print(Fore.CYAN + "Showing All Tickets".center(100))
        for ticket in zenpy_client.search(type='ticket'):
            count += 1

            #Decide if user wants to go to next page of results
            if count > 25 and (count-1) % 25 == 0:
                if Menus.askPage() == True:
                    return(True)
                else:
                    pCount += 1
                    print(Fore.CYAN + ("Showing page " + str(pCount)).center(100))

            time = datetime.strptime(str(ticket.created_at), "%Y-%m-%dT%H:%M:%SZ")
            print(Fore.CYAN + "Ticket with id: " + str(ticket.id) + " | Assigned to: " + str(ticket.assignee_id) + " | created on " + time.strftime("%a %b %d %Y at %I:%M %p")  + " | Ticket Subject: " + str(ticket.subject))

        if count == 0:
            print("No Tickets Available at this time.")

        else:
            print("There are no more available tickets.\n")
        return Menus.returnToTicketMenu()

    except zenpy.lib.exception.APIException:
        print("There was an API error, please check that that the API token is correct.")
        return True

    except requests.exceptions.ConnectionError:
        print("There was a problem connecting to the API. Please check your internet connection.")
        return True