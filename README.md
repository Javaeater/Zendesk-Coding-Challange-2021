# Welcome to Zendesk Ticket Viewer
This is a simple ticket viewer coded for the Zendesk Coding Challange 2021 for the Summer Co-Op position.

The goal of this project was to create a ticket viewing application that connects to the Zendesk API. Users are allowed to view a single ticket on their account as well as all the tickets on their account.

Made by Cesser Jackson in Aug 2021

## Installation MacOS/Windows
Please make sure you have Python 3.9.6 or newer.
 - You can install the newest version of python here: https://www.python.org/downloads/
 - 
 - If the ``` python ``` command is not working please use ``` python3 ``` instead for any use of ``` python ``` in this documentation.

Also, make sure you are using pip 21.2.1 or newer.
 - If you are not sure you have pip installed you can use the command ``` python -m ensurepip --upgrade ```
 - If you have pip installed but not the correct version please use ``` python -m pip install --upgrade pip ```

Clone the repository to your active directory with the command ``` git clone https://github.com/Javaeater/Zendesk-Coding-Challange-2021 ```

Navigate inside the project folder with ``` cd Zendesk-Coding-Challange-2021 ``` 

Then go to the github file inside the repository using ``` cd github ```

Install the required packages using ``` pip install -r requirements.txt ```

## Authentication

The TicketFunctions.py file takes in credentials from the creds.py file.

creds.py contains base64 encrypted strings for the Username, API token, and subdomain.

To add or edit authentication info please change the strings in:

- ``` base64_email ``` to the correct base64 encrypted email address string.

- ``` base64_token ``` to the correct base64 encrypted token string.

- ``` base64_subD ``` to the correct base64 encrypted subdomain string.


## Running

Please navigate to the github folder using ```cd github ```

Run ```Python -m ViewTickets``` 

## Running Tests
Please navigate to the github folder using ```cd github ```

Run ```Python -m test_functions.py``` 

Follow all instructions written in white text.

## How it Works
``` Menus.py ``` Contains functions to create text and menu displays.

``` TicketFunctions.py ``` Contains functions to handle viewing and processing ticket information.

``` ViewTickets.py ``` Main file handles the program as it runs.

``` creds.py ``` Holds Crediental information in base64 format and decodes it to the correct string.

``` test_functions.py ``` Runs unittests.

## Notes 
This program uses colroama to display text in ANSI color to the CLI. 

- It has been tested to work on Window cmd and MacOS terminal.

- If colors are not displayed on MacOs terminal make sure your terminal has the correct settings to display ANSI color. If you need help doing this here is a link to someone explaining it on stack overflow https://stackoverflow.com/questions/1550288/os-x-terminal-colors.

- It should not cause a program issue if using a non supported device. Text may just print in single color

