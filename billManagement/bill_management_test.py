import unittest

from bill_management import read_bills, write_bills

class TestBillManagement(unittest.TestCase):
    
    def test_read_bills(self):
        bills = read_bills()
        self.assertEquals( 20, len(bills)) 
        self.assertEquals( 'Electric Ireland', bills[0][0]) 
        self.assertEquals( 'credit', bills[19][6]) 
        
    def test_write_bills(self):
        bills = read_bills()
        write_bills(bills)
        bills = read_bills()
        self.assertEquals( 20, len(bills)) # after read, write and read again the file should be the same
        self.assertEquals( 'Electric Ireland', bills[0][0]) 
        self.assertEquals( 'credit', bills[19][6]) 
        
#    def test_get_message(self):
#        self.assertEquals()
        
        
if __name__  == '__main__':
    unittest.main()
    