#006a5d4bf0830c2371ff486b61c8eb62d66410e5c89d5695157e751575d8404a

import sys
from zenpy import Zenpy
import json
import argparse
zenpy_client = Zenpy(**creds)

#Inital start menu
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

#view a single ticket
def viewSingle(id):
    try:
        tk = None
        for ticket in zenpy_client.search(type='ticket', query=id):
            tk = ticket
        if tk != None:
            print(tk.url)
        else:
            print("Unable to find ticket id. Make sure you are entering a valid ticket id.\n Returning to ticket menu")

    except zenpy.lib.exception.APIException:
        print("There was an API error, please check ")

#View all tickets
def viewAll():
    try:
        for ticket in zenpy_client.search(type='ticket'):
            print(ticket.url)

    except zenpy.lib.exception.APIException:
        print("There was an API error, please check ")

#display the main menu
def displayMenu():
    print('Ticket Menu'.center(100, "_"))
    print("-- Type 'view' to see in depth information on a single ticket --".center(100))
    print("-- Type 'view all' to see a basic overview of all tickets --".center(96))
    print("-- Type 'qt' to quit the program --".center(71))
    menuSelect = input()
    return(menuSelect)

#main function
if __name__ == '__main__':
    print(f"{'Zendesk Ticket Viewer version 1.0.0' : ^100}")
    run = startTicketView()
    while run:
        ans = displayMenu()
        if ans.lower() == 'view':
            idSelect = input("What ticket would you like to view?")
            viewSingle(idSelect)
        elif ans.lower() == 'view all':
            viewAll()
        elif ans.lower == 'qt':
            run = False
        else:
            print("Invalid entry. Please refer to the menu for ticket options")
    print("Thank you for using the Zendesk Ticket Viewer")