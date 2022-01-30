import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the  Article class.
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new_source = Source('bbc-uk', 'BBC News', 'general', 'https://www.bbc.com')

    def test_init(self):
        self.assertTrue(isinstance(self.new_source, Source))