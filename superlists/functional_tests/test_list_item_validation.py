from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest): 
           
    def test_cannot_add_empty_list_items(self):
        # Edith visits the home page and accidentally tries to submit an empty list item.
        self.browser.get(self.server_url)
        self.browser.get_item_input_box().send_keys('\n')
        
        # The home page refreshes and shows an error message that says list items can't be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        
        # So she enters text, and it works
        self.browser.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')
        
        # She tries again to create an empty list item
        self.browser.get_item_input_box().send_keys('\n')
        
        # And it fails again in the same way
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        
        # She fills in some text and it works
        self.browser.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
        
        
        
