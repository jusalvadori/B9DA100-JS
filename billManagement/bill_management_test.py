import unittest

from bill_management import bill_management

class TestBillManagement(unittest.TestCase):
        
    # this method is called once before before all the tests 
    @classmethod
    def setUpClass(self):
        self.bill_management = bill_management()   
        self.bill_management.read_bills('bills.csv')
    
    def test_a_read_bills(self):        
        # initial file has 24 rows
        self.assertEqual( 24, len(self.bill_management.bills)) 
        # verify that the information in the first column in the first line is 'Eletric Ireland'
        self.assertEqual( 'Electric Ireland', self.bill_management.bills[0][0])  
        # verify that the information in the 7th column in the 20th line (last line/last column) is 'credit' 
        self.assertEqual( 'credit', self.bill_management.bills[19][6]) 
    
    def test_b_write_bills(self):
        self.bill_management.write_bills('bills.csv')  # write list of bills back to the file
        self.bill_management.read_bills('bills.csv')   # read file again
        # after read, write and read again, the file should be the same
        # file should have 24 lines
        self.assertEqual( 24, len(self.bill_management.bills)) 
        # verify that the information in the first column in the first line is still 'Eletric Ireland'
        self.assertEqual( 'Electric Ireland', self.bill_management.bills[0][0]) 
        # verify that the information in the 7th column in the 20th line (last line/last column) is still 'credit'
        self.assertEqual( 'credit', self.bill_management.bills[19][6]) 
        
    def test_c_insert_bill(self):
        self.bill_management.insert_bill('Board Gais', 'Juliana', '15-11-2019', 115.38, 2)
        self.bill_management.write_bills('bills.csv')  # write list of bills back to the file
        self.bill_management.read_bills('bills.csv')   # read the file again 
        # the file should has 25 rows
        self.assertEqual( 25, len(self.bill_management.bills)) 
        # check if each column from the lasst line is correct as per information inserted
        self.assertEqual( 'Board Gais', self.bill_management.bills[-1][0])         
        self.assertEqual( 'Juliana', self.bill_management.bills[-1][1])         
        self.assertEqual( '2019', self.bill_management.bills[-1][2])        
        self.assertEqual( '11', self.bill_management.bills[-1][3])         
        self.assertEqual( '15', self.bill_management.bills[-1][4])        
        self.assertEqual( '115.38', self.bill_management.bills[-1][5])        
        self.assertEqual( 'debit', self.bill_management.bills[-1][6]) 
        
    def test_d_total_by_year(self):
        total_year = self.bill_management.total_by_year()  
        self.assertEqual( '2016', total_year[0]['year'])   
        self.assertEqual( 5.0, round(total_year[0]['credit'],2) )
        self.assertEqual( 167.52, round(total_year[0]['debit'],2) )
        
    def test_e_most_popular_company(self):
        most_popular = self.bill_management.most_popular_company()  
        self.assertEqual( 'Vodafone', most_popular[0][0])   
        self.assertEqual( 10, most_popular[0][1])
        
    def test_f_order_bills_by_date(self):
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
        # hightest credit amount
        sorted_by_credit = self.bill_management.highest_amount('credit')        
        self.assertEqual( 'Electric Ireland', sorted_by_credit[0][0])  
        self.assertEqual( 'John Smyth', sorted_by_credit[0][1] )
        self.assertEqual( '81.58', sorted_by_credit[0][5] )   
        self.assertEqual( 'credit', sorted_by_credit[0][6] )
        
    def test_h_highest_amount_debit(self):  
        # highest debit amount
        sorted_by_debit  = self.bill_management.highest_amount('debit')
        self.assertEqual( 'Energia', sorted_by_debit[0][0])  
        self.assertEqual( 'Missy May', sorted_by_debit[0][1] )
        self.assertEqual( '152.52', sorted_by_debit[0][5] )   
        self.assertEqual( 'debit', sorted_by_debit[0][6] )        
        
    def test_i_average_spent_per_period(self):
        # average spent per period of time
        avg_per_period  = self.bill_management.average_spent_per_period('')
        self.assertEqual( '2016', next(avg_per_period.iterrows())[0][0] )  
        self.assertEqual( '11', next(avg_per_period.iterrows())[0][1] )  
        self.assertEqual( 22.50, next(avg_per_period.iterrows())[1][0] ) 
        
        avg_per_period  = self.bill_management.average_spent_per_period('11-2018')
        self.assertEqual( '2018', next(avg_per_period.iterrows())[0][0] )  
        self.assertEqual( '11', next(avg_per_period.iterrows())[0][1] )  
        self.assertEqual( 27.5, next(avg_per_period.iterrows())[1][0] ) 
        
    def test_j_average_time_between_bills(self): 
        # average spent per period of time
        avg_time  = self.bill_management.average_time_between_bills()
        self.assertEqual( 47.67 , avg_time )  
        
    # this method is called once after all the tests have run
    @classmethod
    def tearDownClass (self):
        # restore the original test file
        self.bill_management.read_bills('bills-Copy.csv')   # read the initial file
        self.bill_management.write_bills('bills.csv')  # write list of bills back to the file
        self.bill_management.read_bills('bills.csv')   # read file again
        
        
if __name__  == '__main__':
    unittest.main()
    