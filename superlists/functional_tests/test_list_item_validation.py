from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest): 
           
    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')
    
           
    def test_cannot_add_empty_list_items(self):
        # Edith visits the home page and accidentally tries to submit an empty list item.
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        
        # The home page refreshes and shows an error message that says list items can't be blank
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")
        
        # So she enters text, and it works
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')
        
        # She tries again to create an empty list item
        self.get_item_input_box().send_keys('\n')
        
        # And it fails again in the same way
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")
        
        # She fills in some text and it works
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
        
        
    def test_cannot_add_duplicate_items(self):
        # Edith visits the home page and starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')
        
        # accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies\n')
        
        # and sees a helpful error message
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")
        
        
    def test_error_messages_are_cleared_on_correct_input(self):
        # Edit starts a new list in a way that causes a validation error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())
        
        # she starts typing in the input box, which should clear the error
        self.get_item_input_box().send_keys('a')
        
        # and is pleased when the error message disappears w/o a page refresh
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())
        
        
