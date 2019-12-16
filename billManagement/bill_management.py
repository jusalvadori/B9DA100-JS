import datetime

class bill_management(object):
    def __init__(self):
        self.bills = []

    def read_bills(self):
        self.bills = []
        bills_file = open('bills.csv') 
        for line in bills_file: 
            self.bills.append(line.strip().split(',')) 
            self.bills[-1][-1] = self.bills[-1][-1].strip()  
    
    def write_bills(self):
        with open('bills.csv', mode='w') as bill_file:
            for bill in self.bills:            
                bill_file.write(', '.join(bill) + '\n')
    
    def display_menu(self):
        print('Welcome to bill management company') 
        print('1: View bills\n2: Insert a bill\n3: Reports\n4: T&C\n5: Exit') 
        
    def view_bills(self):
        for bill in self.bills:
            print(bill[0], bill[1], bill[2], bill[3], bill[4], bill[5], bill[6])
            
    def insert_bill(self, pi_company, pi_customer, pi_date, pi_amount, pi_deb_cred):
        row = len(self.bills) + 1
        self.bills[row][0] = pi_company
        self.bills[row][1] = pi_customer
        self.bills[row][2] = datetime.datetime.strptime(pi_date, '%Y-%m-%d').date().year
        self.bills[row][3] = datetime.datetime.strptime(pi_date, '%Y-%m-%d').date().month
        self.bills[row][4] = datetime.datetime.strptime(pi_date, '%Y-%m-%d').date().day
        self.bills[row][5] = pi_amount
        self.bills[row][6] = pi_deb_cred

        
    def process_choice(self):
        choice = input('Please enter an option:') 
        while choice != '5':    # check the version of python to identify the type of return from input function 
            if choice == '1':
                self.view_bills()
                
            elif choice == '2':
                self.insert_bill()
        
            
            choice = input('Please enter an option:') 


            
    def main(self):
        self.read_bills()
        self.display_menu()
        self.process_choice()
        self.write_bills()  # before leaving the application save the list of bills
    
if __name__  == '__main__':
    bill_management = bill_management()
    bill_management.main()