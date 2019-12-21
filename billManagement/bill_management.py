import datetime

class bill_management(object):
    def __init__(self):
        self.bills = []

    def read_bills(self): 
        self.bills = []
        bills_file = open('bills.csv') 
        for line in bills_file: 
            self.bills.append(line.strip().split(',')) 
            #remove leading/trailing space from each column for the line appended
            for col in range(0,len(self.bills[-1])): 
                self.bills[-1][col] = self.bills[-1][col].strip()     
    
    def write_bills(self):
        with open('bills.csv', mode='w') as bill_file:
            for bill in self.bills: 
                bill_file.write(', '.join(bill) + '\n')
    
    def display_menu(self):
        print('*********************************************************************************')
        print('Welcome to Bill Management Company') 
        print('1: View bills\n2: Insert a bill\n3: Reports\n4: T&C\n5: Exit') 
        
    def view_bills(self):
        print('%20s'%'Company', '%20s'%'Customer', '%5s'%'Year', '%5s'%'Month', '%5s'%'Day', '%10s'%'Amount', '%10s'%'Type')    
        for bill in self.bills:
            print('%20s' % bill[0], '%20s' % bill[1], '%5s' % bill[2], '%5s' % bill[3], '%5s' % bill[4], '%10s' % bill[5], '%10s' % bill[6])
            
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
    
    def get_input_string(self, prompt):
        value = input(prompt)
        while not value:
            value = input(prompt)
            
        return value
    
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
                      
                           
            
    def main(self):
        self.read_bills()
        self.process_choice()
        self.write_bills()  # before leaving the application save the list of bills
    
if __name__  == '__main__':
    bill_management = bill_management()
    bill_management.main()