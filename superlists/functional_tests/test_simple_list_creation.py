from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys        
       
class NewVisitorTest(FunctionalTest):
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith retrieves the home page
        self.browser.get(self.server_url)

        # notices page title and header, which both mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # invited to enter a to-do right away
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # types 'buy peacock feathers' into a text box
        inputbox.send_keys('Buy peacock feathers')

        # hits enter, a new URL (for the particular list) is retrieved, and the page now lists the item as a to-do
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # the entry text box is still there, use it to enter a to-do to make a fly fishing lure
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        
        # the page updates again, to show both items on the list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        
        # now a new user - Francis - visits the site
        ## use a new browser session to make sure no information of Edith's comes through via cookies, etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        # Francis visits home page - no sign of Edith's list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        
        # Francis starts a new list by entering an item
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        
        # Francis has his own URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        
        # again, no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
    
        
        
        
