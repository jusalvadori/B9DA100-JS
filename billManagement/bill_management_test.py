import unittest

from bill_management import bill_management

class TestBillManagement(unittest.TestCase):
    
    # this method is executed before each test method
    def setUp(self):
        self.bill_management = bill_management()
      
    
    def test_read_bills(self):
        self.bill_management.read_bills()
        # initial file has 20 rows
        self.assertEquals( 20, len(self.bill_management.bills)) 
        # verify that the information in the first column in the first line is 'Eletric Ireland'
        self.assertEquals( 'Electric Ireland', self.bill_management.bills[0][0])  
        # verify that the information in the 7th column in the 20th line (last line/last column) is 'credit' 
        self.assertEquals( 'credit', self.bill_management.bills[19][6]) 
        
    def test_write_bills(self):
        self.bill_management.read_bills()   # read the initial file
        self.bill_management.write_bills()  # write list of bills back to the file
        self.bill_management.read_bills()   # read file again
        # after read, write and read again, the file should be the same
        # file should have 20 lines
        self.assertEquals( 20, len(self.bill_management.bills)) 
        # verify that the information in the first column in the first line is still 'Eletric Ireland'
        self.assertEquals( 'Electric Ireland', self.bill_management.bills[0][0]) 
        # verify that the information in the 7th column in the 20th line (last line/last column) is still 'credit'
        self.assertEquals( 'credit', self.bill_management.bills[19][6]) 
        
    def test_insert_bill(self):
        self.bill_management.read_bills()   # read the initial file
        self.bill_management.insert_bill()
        self.bill_management.write_bills()  # write list of bills back to the file
        self.bill_management.read_bills()   # read the file again 
        # the file should has 21 rows
        self.assertEquals( 21, len(self.bill_management.bills)) 
        
        self.assertEquals( 'credit', self.bill_management.bills[20][0]) 
        
        self.assertEquals( 'credit', self.bill_management.bills[20][1]) 
        
        self.assertEquals( 'credit', self.bill_management.bills[20][2])
        
        self.assertEquals( 'credit', self.bill_management.bills[20][3]) 
        
        self.assertEquals( 'credit', self.bill_management.bills[20][4])
        
        self.assertEquals( 'credit', self.bill_management.bills[20][5])
        
        self.assertEquals( 'credit', self.bill_management.bills[20][6]) 
        
        
if __name__  == '__main__':
    unittest.main()
    