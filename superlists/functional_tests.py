from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith retrieves the home page
        self.browser.get('http://localhost:8000')

        # notices page title and header, which both mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # invited to enter a to-do right away

        # types 'buy peacock feathers' into a text box

        # hits enter, the page updates, and the page now lists the item as a to-do

        # the entry text box is still there, use it to enter a to-do to make a fly fishing lure

        # the page updates again, and now shows both items

        # will the page remember the list? oh, it's generated a unique URL for her and has text that explains this

        # visit the URL - the list is still there
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')