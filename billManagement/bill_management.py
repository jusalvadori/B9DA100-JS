#import csv

def read_bills():
    
    return [ [col.strip() for col in line.strip().split(',') ] for line in open('bills.csv') if len(line) > 1 ] 
    
#    bills = [] 
#    bills_file = open('bills.csv') 
#    for line in bills_file: 
#        bills.append(line.strip().split(',')) 
#        bills[-1][-1] = bills[-1][-1].strip()  
#    return bills  

def display_menu():
    print('Welcome to bill management company') 
    print('1: View bills\n2: Insert a bill\n3: Reports\n4:T&C\n5: Exit') 
    
def view_bills(bills):
    for bill in bills:
        print(bill[0], bill[1], bill[3], bill[4], bill[5], bill[6])
    
def process_choice(bills):
    choice = input('Please enter an option:') 
    while choice != '5':    # check the version of python to identify the type of return from input function 
        if choice == '1':
            view_bills(bills)
        
        choice = input('Please enter an option:') 

def write_bills(bills):
    with open('bills.csv', mode='w') as bill_file:
        for bill in bills:            
            #bill_file.write(', '.join(bill))  # this returns an error (add to the test file) as it will write everything in the same line
            bill_file.write(', '.join(bill) + '\n')
            
def main():
    bills = read_bills()
    display_menu()
    process_choice(bills)
    write_bills(bills)  # before leaving the application salve the list of bills
    
if __name__  == '__main__':
    main()