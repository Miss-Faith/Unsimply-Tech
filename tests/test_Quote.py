import unittest
from app.models import Quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote("author","id","Quote")

    def test_instance(self):
        '''
        Test to check creation of new quote instance
        '''
        self.assertTrue(isinstance(self.new_quote,Quote))

    def test_save_quote(self):
        '''
        Test to check if instance variables are saved
        '''
        self.new_quote.save_quote()
        self.assertTrue(len(Quote.all_quotes),1)


if __name__ == '__main__':
    unittest.main()