import unittest

from bill_management import bill_management

class TestBillManagement(unittest.TestCase):
        
    # this method is executed before each test method
    def setUp(self):
        self.bill_management = bill_management()          
    
    def test_a_read_bills(self):
        self.bill_management.read_bills('bills.csv')
        # initial file has 20 rows
        self.assertEqual( 20, len(self.bill_management.bills)) 
        # verify that the information in the first column in the first line is 'Eletric Ireland'
        self.assertEqual( 'Electric Ireland', self.bill_management.bills[0][0])  
        # verify that the information in the 7th column in the 20th line (last line/last column) is 'credit' 
        self.assertEqual( 'credit', self.bill_management.bills[19][6]) 
    
    def test_b_write_bills(self):
        self.bill_management.read_bills('bills.csv')   # read the initial file
        self.bill_management.write_bills('bills.csv')  # write list of bills back to the file
        self.bill_management.read_bills('bills.csv')   # read file again
        # after read, write and read again, the file should be the same
        # file should have 20 lines
        self.assertEqual( 20, len(self.bill_management.bills)) 
        # verify that the information in the first column in the first line is still 'Eletric Ireland'
        self.assertEqual( 'Electric Ireland', self.bill_management.bills[0][0]) 
        # verify that the information in the 7th column in the 20th line (last line/last column) is still 'credit'
        self.assertEqual( 'credit', self.bill_management.bills[19][6]) 
        
    def test_c_insert_bill(self):
        self.bill_management.read_bills('bills.csv')   # read the initial file
        self.bill_management.insert_bill('Board Gais', 'Juliana', '15-11-2019', 115.38, 2)
        self.bill_management.write_bills('bills.csv')  # write list of bills back to the file
        self.bill_management.read_bills('bills.csv')   # read the file again 
        # the file should has 21 rows
        self.assertEqual( 21, len(self.bill_management.bills)) 
        # check if each column from the lasst line is correct as per information inserted
        self.assertEqual( 'Board Gais', self.bill_management.bills[20][0])         
        self.assertEqual( 'Juliana', self.bill_management.bills[20][1])         
        self.assertEqual( '2019', self.bill_management.bills[20][2])        
        self.assertEqual( '11', self.bill_management.bills[20][3])         
        self.assertEqual( '15', self.bill_management.bills[20][4])        
        self.assertEqual( '115.38', self.bill_management.bills[20][5])        
        self.assertEqual( 'debit', self.bill_management.bills[20][6]) 
        
    def test_d_total_by_year(self):
        self.bill_management.read_bills('bills.csv')  # read the initial file
        total_year = self.bill_management.total_by_year()  
        self.assertEqual( '2016', total_year[0]['year'])   
        self.assertEqual( 5.0, round(total_year[0]['credit'],2) )
        self.assertEqual( 167.52, round(total_year[0]['debit'],2) )
        
    def test_e_most_popular_company(self):
        self.bill_management.read_bills('bills.csv')  # read the initial file
        most_popular = self.bill_management.most_popular_company()  
        self.assertEqual( 'Vodafone', most_popular[0][0])   
        self.assertEqual( 8, most_popular[0][1])
        
    def test_f_total_by_year(self):
        self.bill_management.read_bills('bills.csv')  # read the initial file
        ordered_bills = self.bill_management.order_bills_by_date()  
        # first bill by date
        self.assertEqual( 'Energia', ordered_bills[0]['company'])   
        self.assertEqual( 'Susie Sue', ordered_bills[0]['customer'] )
        self.assertEqual( '2016-11-03', ordered_bills[0]['date'].strftime('%Y-%m-%d') )
        # last bill by date
        self.assertEqual( 'Energia', ordered_bills[-1]['company'])   
        self.assertEqual( 'Missy May', ordered_bills[-1]['customer'] )
        self.assertEqual( '2019-12-22', ordered_bills[-1]['date'].strftime('%Y-%m-%d'))
  
    def test_g_highest_amount_credit(self):
        self.bill_management.read_bills('bills.csv')  # read the initial file    
        # hightest credit amount
        sorted_by_credit = self.bill_management.highest_amount('credit')        
        self.assertEqual( 'Electric Ireland', sorted_by_credit[0][0])  
        self.assertEqual( 'John Smyth', sorted_by_credit[0][1] )
        self.assertEqual( '81.58', sorted_by_credit[0][5] )   
        self.assertEqual( 'credit', sorted_by_credit[0][6] )
        
    def test_h_highest_amount_debit(self):  
        self.bill_management.read_bills('bills.csv')  # read the initial file 
        # highest debit amount
        sorted_by_debit  = self.bill_management.highest_amount('debit')
        self.assertEqual( 'Energia', sorted_by_debit[0][0])  
        self.assertEqual( 'Missy May', sorted_by_debit[0][1] )
        self.assertEqual( '152.52', sorted_by_debit[0][5] )   
        self.assertEqual( 'debit', sorted_by_debit[0][6] )        
        
    def test_i_average_spent_per_period(self):
        self.bill_management.read_bills('bills.csv')  # read the initial file 
        # average spent per period of time
        avg_per_period  = self.bill_management.average_spent_per_period()
        self.assertEqual( '2016', next(avg_per_period.iterrows())[0][0] )  
        self.assertEqual( '11', next(avg_per_period.iterrows())[0][1] )  
        self.assertEqual( 22.5, next(avg_per_period.iterrows())[1][0] )  
        
if __name__  == '__main__':
    unittest.main()
    