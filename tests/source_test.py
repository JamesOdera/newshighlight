import unittest
from models import Source,Articles

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source(1234,'Python Must Be Crazy','A thrilling new Python Series','https://newsapi.org/v2/sources?apikey={}&query={}',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('CNN','Peter Polle','The tech scene in Africa-Is it the next big thing?','A look at various tech hubs in Africa and the impact they have on the worlds economy','techie.com','techie.com/7643t94.jpg','2018-04-11T07:57:16Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))



