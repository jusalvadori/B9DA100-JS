import datetime

class bill_management(object):
    def __init__(self):
        self.bills = []

    #############################################################################################################
    # Read bills from csv file
    def read_bills(self, file_name): 
        self.bills = []
        bills_file = open(file_name) 
        for line in bills_file: 
            self.bills.append(line.strip().split(',')) 
            #remove leading/trailing space from each column for the line appended
            for col in range(0,len(self.bills[-1])): 
                self.bills[-1][col] = self.bills[-1][col].strip()     
    
    #############################################################################################################
    # Write list of bills back to the csv file
    def write_bills(self, file_name):
        with open(file_name, mode='w') as bill_file:
            for bill in self.bills: 
                bill_file.write(', '.join(bill) + '\n')
                
    #############################################################################################################
    # Display list of bills 
    def view_bills(self):
        print('%20s'%'Company', '%20s'%'Customer', '%5s'%'Year', '%5s'%'Month', '%5s'%'Day', '%10s'%'Amount', '%10s'%'Type')    
        for bill in self.bills:
            print('%20s' % bill[0], '%20s' % bill[1], '%5s' % bill[2], '%5s' % bill[3], '%5s' % bill[4], '%10s' % bill[5], '%10s' % bill[6])
    
    #############################################################################################################
    # Insert a new bill to the current list
    def insert_bill(self, pi_company, pi_customer, pi_date, pi_amount, pi_deb_cred):
        if pi_deb_cred == 1: 
            p_type = 'credit' 
        else: p_type = 'debit' 
        
        self.bills.append( [pi_company
                        , pi_customer
                        , str(datetime.datetime.strptime(pi_date, '%d-%m-%Y').date().year)
                        , str(datetime.datetime.strptime(pi_date, '%d-%m-%Y').date().month)
                        , str(datetime.datetime.strptime(pi_date, '%d-%m-%Y').date().day)
                        , str(pi_amount)
                        , p_type ] )
    
    #############################################################################################################
    # Receive a string input
    def get_input_string(self, prompt):
        value = input(prompt)
        while not value:
            value = input(prompt)
            
        return value
   
    #############################################################################################################
    # Receive a date input from the user
    def get_input_date(self, prompt):
        while True:
            value = input(prompt)
            try:
                datetime.datetime.strptime(value, '%d-%m-%Y')
               # print('The date {} is valid.'.format(value))
            except ValueError:
                print('The date {} is invalid'.format(value))
                continue
            
            break
            
        return value
    
    #############################################################################################################
    # Receive a number input from the user    
    def get_input_number(self, prompt, p_type):
        while True:
            try:
                if p_type == 1:
                    value = float(input(prompt))
                else:
                    value = int(input(prompt))
            except ValueError:
                print("**Sorry, I didn't understand your response.")
                continue
    
            if value < 0:
                print("**Sorry, your response must not be negative.")
                continue            
            elif p_type == 2 and value not in (1,2):
                print("**Sorry, your response must be 1=Credit or 2=Debit.")
                continue            
            else:
                break
        return value
    
    #############################################################################################################
    # Report 1:
    # function to calculate total credited and total debited for each year
    def total_by_year(self):
        total_year = [] 
        for bill in self.bills:
            if bill[6] == 'credit':
                tcred  = float(bill[5])
                tdeb   = 0
            else:
                tcred  = 0
                tdeb   = float(bill[5])
            
            found = 0
            if len(total_year) > 0:                
                for index in range(len(total_year)):
                    if bill[2] == total_year[index]['year']: 
                        found = 1
                        total_year[index]['credit'] += tcred
                        total_year[index]['debit']  += tdeb
                            
            if found == 0:
                total_year.append( {'year': bill[2] , 'credit': tcred , 'debit': tdeb} )
        
        # order the result list by year
        total_year = sorted(total_year, key = lambda i: i['year'])
        
        return total_year                
    
    #############################################################################################################
    # Report 1:
    # This report lists total credited and total debited for each year
    def display_total_by_year(self):
        total_year = self.total_by_year()
        
        print('\n---------------------------------------------------------------------------------')
        print('\nTotal by year')
        print('%5s'%'Year', '%20s'%'Total credited', '%20s'%'Total debited')  
        for index in range(len(total_year)):
            print('%5s' % total_year[index]['year'], '%20s' % round(total_year[index]['credit'],2), '%20s' % round(total_year[index]['debit'],2) )
        
    #############################################################################################################
    # Report 2:
    # function to calculate the most popular utility company
    def most_popular_company(self):
        most_popular = {} 
        for bill in self.bills:    
            if bill[0] in most_popular:
                most_popular[bill[0]] += 1
            else:
                most_popular[bill[0]] = 1
        
        most_popular = sorted (most_popular.items() , reverse=True)
        return most_popular
        
    #############################################################################################################
    # Report 2:
    # This report lists the most popular utility company by number of bills
    def display_most_popular_company(self):
        most_popular = self.most_popular_company()        
        
        print('\n---------------------------------------------------------------------------------')
        print('\nMost popular utility company')
        print('%20s'%'Company', '%10s'%'Number of bills')  
        for company in most_popular:
            print('%20s' % company[0], '%10s' % company[1] )

            
    #############################################################################################################
    # Display main menu
    def display_menu(self):
        print('\n*********************************************************************************')
        print('Welcome to Bill Management Company') 
        print('1: View bills\n2: Insert a bill\n3: Reports\n4: T&C\n5: Exit') 
        
    #############################################################################################################
    # Display reports menu
    def display_reports_menu(self):
        print('\n---------------------------------------------------------------------------------')
        print('Reports available:') 
        print('1: Total by year\n2: Most popular utility company\n3: Bills in date order\n4: Highest amount by bill type\n5: Number of bills by company \n6: Average spent per period of time \n7: Average time between bills \n8: Return') 

    #############################################################################################################
    # Process user choice - reports menu
    def process_report_choice(self):
        report_choice = None
        while report_choice != '8':    # check the version of python to identify the type of return from input function 
            self.display_reports_menu()
            report_choice = input('Please enter an option:') 
            
            if report_choice == '1':
                self.display_total_by_year()
            
            elif report_choice == '2':
                self.display_most_popular_company()
                
                
                
        
    #############################################################################################################
    # Process user choice - main menu
    def process_choice(self):
        choice = None
        while choice != '5':    # check the version of python to identify the type of return from input function 
            self.display_menu()
            choice = input('Please enter an option:') 
            
            if choice == '1':
                self.view_bills()                         
                
            elif choice == '2':
                bill_company  = self.get_input_string('Please enter the company name: ')
                bill_customer = self.get_input_string('Please enter the customer name: ')
                bill_date     = self.get_input_date('Please enter the bill date (dd-mm-yyyy): ')
                bill_amount   = self.get_input_number('Please enter the bill amount: ',1)
                bill_type     = self.get_input_number('Please enter the bill type (1=Credit or 2=Debit): ',2)
                self.insert_bill(bill_company,bill_customer,bill_date,bill_amount,bill_type)
                      
            elif choice == '3':
                self.process_report_choice()    
                           
            
    def main(self):
        self.read_bills('bills.csv')
        self.process_choice()
        self.write_bills('bills.csv')  # before leaving the application save the list of bills
    
if __name__  == '__main__':
    bill_management = bill_management()
    bill_management.main()