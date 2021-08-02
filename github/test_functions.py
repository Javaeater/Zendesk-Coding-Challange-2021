import unittest
import Menus
import ViewTickets
import TicketFunctions
import zenpy
from colorama import Fore, Style, init

#make sure colorama will work on device
init(convert=True)

class TestViewer(unittest.TestCase):
    # Test startTicketView with op
    def test_StartTicketViewTrue(self):
        print(Fore.RESET + "For this test please type 'op'")
        self.assertTrue(Menus.startTicketView())

    # Test startTicketView with qt
    def test_StartTicketViewFalse(self):
        print(Fore.RESET + "For this test please type 'qt'")
        self.assertFalse(Menus.startTicketView())

    # Test returnToTicketMenu with y
    def test_returnToTicketMenuTrue(self):
        print(Fore.RESET + "For this test please type 'y'")
        self.assertTrue(Menus.returnToTicketMenu())

    # Test returnToTicketMenu with qt
    def test_returnToTicketMenuFalse(self):
        print(Fore.RESET + "For this test please type 'qt'")
        self.assertFalse(Menus.returnToTicketMenu())

    # Test returnToTicketMenu with random input
    def test_returnToTicketMenuTrue2(self):
        print(Fore.RESET + "For this test please type a random string.")
        self.assertTrue(Menus.returnToTicketMenu())

    # Test askPage with tm
    def test_askPageFalse(self):
        print(Fore.RESET + "For this test please type tm")
        self.assertTrue(Menus.askPage())

    # Test askPage with random input
    def test_askPageTrue(self):
        print(Fore.RESET + "For this test please type a random string")
        self.assertTrue(Menus.askPage())

    # Test askPage with y
    def test_askPageTrue2(self):
        print(Fore.RESET + "For this test please type y")
        self.assertFalse(Menus.askPage())

    # Test viewing a single ticket with invalid id
    def test_viewSingleInvalid(self):
        print(Fore.RESET + "Testing non eixistant ticket id")
        self.assertTrue(TicketFunctions.viewSingle("134675"))

    # Test viewing a single ticket with wrong format id
    def test_viewSingleWrongFormat(self):
        print(Fore.RESET + "Testing wrong input format for ticket id")
        self.assertTrue(TicketFunctions.viewSingle("134fghf5"))

    # Test viewing a single valid ticket with answer 'y'
    def test_viewSingleValid(self):
        print(Fore.RESET + "For this test please type 'y'")
        self.assertTrue(TicketFunctions.viewSingle("1"))

    # Test viewing a single valid ticket with a random string
    def test_viewSingleValid2(self):
        print(Fore.RESET + "For this test please type a 'random string'")
        self.assertTrue(TicketFunctions.viewSingle("1"))

    # Test viewing a single valid ticket with answer 'qt'
    def test_viewSingleValid3(self):
        print(Fore.RESET + "For this test type 'qt'")
        self.assertFalse(TicketFunctions.viewSingle("1"))

    # Test viewing pages return to ticket menu
    def test_viewAllNoNewPage(self):
        print(Fore.RESET + "For this test please type tm when asked if wanted to view a new page")
        self.assertTrue(TicketFunctions.viewAll())

    # Test viewing pages random string on new page
    def test_viewAllNoNewPage1(self):
        print(Fore.RESET + "For this test please type a random string when asked if wanted to view a new page")
        self.assertTrue(TicketFunctions.viewAll())

    # Test all tickets paged then answer 'y'
    def test_viewAllNewPages(self):
        print(Fore.RESET + "For this test please page through all tickets until no more are available. Then type y when asked to return to the ticket menu.")
        self.assertTrue(TicketFunctions.viewAll())

    # Test all tickets paged then answer 'qt'
    def test_viewAllNewPages1(self):
        print(Fore.RESET + "For this test please page through all tickets until no more are available. Then type qt when asked to return to the ticket menu.")
        self.assertFalse(TicketFunctions.viewAll())

    # Test all tickets paged then random string.
    def test_viewAllNewPages2(self):
        print(Fore.RESET + "For this test please page through all tickets until no more are available. Then type a random string when asked to return to the ticket menu.")
        self.assertTrue(TicketFunctions.viewAll())

if __name__ == "__main__":
    unittest.main()