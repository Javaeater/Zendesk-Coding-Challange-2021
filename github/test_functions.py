import unittest
import Menus
import ViewTickets
import TicketFunctions

class TestViewer(unittest.TestCase):
    #Test startTicketView with op
    def test_StartTicketViewTrue(self):
        print("For this test please type 'op'")
        self.assertTrue(Menus.startTicketView())

    # Test startTicketView with qt
    def test_StartTicketViewFalse(self):
        print("For this test please type 'qt'")
        self.assertFalse(Menus.startTicketView())

    # Test returnToTicketMenu with y
    def test_returnToTicketMenuTrue(self):
        print("For this test please type 'y'")
        self.assertTrue(Menus.returnToTicketMenu())

    # Test returnToTicketMenu with qt
    def test_returnToTicketMenuFalse(self):
        print("For this test please type 'qt'")
        self.assertFalse(Menus.returnToTicketMenu())

    # Test returnToTicketMenu with random input
    def test_returnToTicketMenuTrue2(self):
        print("For this test please type a random string.")
        self.assertTrue(Menus.returnToTicketMenu())

    #Test askPage with tm
    def test_askPageFalse(self):
        print("For this test please type tm")
        self.assertTrue(Menus.askPage())

    # Test askPage with random input
    def test_askPageTrue(self):
        print("For this test please type a random string")
        self.assertTrue(Menus.askPage())

    # Test askPage with y
    def test_askPageTrue2(self):
        print("For this test please type y")
        self.assertFalse(Menus.askPage())

    def test_viewSingleInvalid(self):
        print("Testing invalid ticket id")
        self.assertTrue(TicketFunctions.viewSingle("1345368644565765783465458776"))

    def test_viewSingleValid(self):
        print("For this test please type 'y'")
        self.assertTrue(TicketFunctions.viewSingle("1"))

    def test_viewSingleValid2(self):
        print("For this test please type a 'random string'")
        self.assertTrue(TicketFunctions.viewSingle("1"))

    def test_viewSingleValid3(self):
        print("For this test type 'qt'")
        self.assertFalse(TicketFunctions.viewSingle("1"))

    def test_viewAllNoNewPage(self):
        print("For this test please type tm when asked if wanted to view a new page")
        self.assertTrue(TicketFunctions.viewAll())

    def test_viewAllNoNewPage1(self):
        print("For this test please type a random string when asked if wanted to view a new page")
        self.assertTrue(TicketFunctions.viewAll())

    def test_viewAllNewPages(self):
        print("For this test please page through all tickets until no more are available. Then type y when asked to return to the ticket menu.")
        self.assertTrue(TicketFunctions.viewAll())

    def test_viewAllNewPages1(self):
        print("For this test please page through all tickets until no more are available. Then type qt when asked to return to the ticket menu.")
        self.assertFalse(TicketFunctions.viewAll())

    def test_viewAllNewPages2(self):
        print("For this test please page through all tickets until no more are available. Then type a random string when asked to return to the ticket menu.")
        self.assertTrue(TicketFunctions.viewAll())

if __name__ == "__main__":
    unittest.main()