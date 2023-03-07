import random
import xlsxwriter
import openpyxl

customers = []

def show_customers():
    print('\n' + '-'*30)
    print('Registered customers:'.center(30))
    print('-'*30)
    for customer in customers:
        print(f'- ID: {customer["id"]}, Name: {customer["name"]}')
    print('-'*30)

def register_customer():
    print('\n' + '-'*30)
    name = input('Enter the name of the new customer: ')
    id = random.randint(10000, 99999)
    customers.append({'id': id, 'name': name})
    print(f'Customer {name} with ID {id} registered successfully.')
    print('-'*30)

def leave_system():
    try:
        workbook = openpyxl.load_workbook('customers.xlsx')
        worksheet = workbook.active
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.append(['ID', 'Name'])
    
    for customer in customers:
        worksheet.append([customer['id'], customer['name']])
    
    workbook.save('customers.xlsx')
    
    print('\n' + '-'*30)
    print('Exiting system...'.center(30))
    
def show_menu():
   while True:
       print('\n' + '-'*30)
       print('Menu:'.center(30))
       print('-'*30)
       print('1 - See registered customers')
       print('2 - Register new customer')
       print('3 - Leave system')
       option = int(input('Enter your option: '))
       if option == 1:
           show_customers()
       elif option == 2:
           register_customer()
       elif option == 3:
           leave_system()
           break
       else:
           print('\n' + '-'*30)
           print('Invalid option. Try again.'.center(30))
           print('-'*30)

show_menu()