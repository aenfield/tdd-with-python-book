from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest): 
           
    def test_cannot_add_empty_list_items(self):
        # Edith visits the home page and accidentally tries to submit an empty list item.
        
        # The home page refreshes and shows an error message that says list items can't be blank
        
        # So she enters text, and it works
        
        # She tries again to create an empty list item
        
        # And it fails again in the same way
        
        # She fills in some text and it works
        
        self.fail("Not implemented yet.")
        
        
        
