''' 
    This program is developed by a group of the 5 students.
    This program is a vegetable & fruit store management system. 
    It allows users to create an account, sign in, buy 
    vegetables, and view their receipts
'''
# Import necessary modules
import getpass  # Module to input passwords without echoing
import time  # Module for time-related functions
from pathlib import Path
# Initialize variables
  # Stores user purchases

# The database containing user information, vegetables, and fruits
database = {     #The Whole Database . 
    'user' : {
        'aaronshenny':{
            'name' : 'Aaron Shenny',
            'password' : '123'
        },                                            
        'user':{                         #Default user

            'name' : 'Guest',
            'password' :'root'
        },                  
        'aswinaravind27':{
            'name' : 'Aswin Aravind',    #User database
            'password':'aswi'

          
        },
        'admin' : {
            'name' : 'ADMIN',
            'password' : 'admin'
        }
    },
    'vegetables':{
        'tomato' : {
            'name' : 'Tomato',
            'price' : '48RS',
                'stock' : 10            #Vegetable Database
        },
        'onion': {
            'name':'Onion',
            'price':'79RS',
            'stock':15
        },
        'green chilli':{
            'name':'Green chilli',
            'price':'46RS',
            'stock':12
        },
        'beetroot':{
            'name':'Beetroot',
            'price':'34RS',
            'stock':14                               
        },
        'potato':{
            'name':'Potato',
            'price':'40RS',
            'stock':16
        },
        'cabbage':{
            'name':'Cabbage',
            'price':'25RS',
            'stock': 13
        },
        'carrot':{
            'name':'Carrot',
            'price':'39RS',
            'stock':17
        
        },
        'corn':{
            'name':'Corn',
            'price':'35RS',
            'stock':19
        },
        'coconut':{
            'name':'Coconut',
            'price':'37RS',
            'stock':16
        },
        'ginger':{
            'name':'Ginger',
            'price':'111RS',
            'stock':20
        },
        'elephant yam':{
            'name':'Elephant Yam',
            'price':'34RS',
            'stock':15
        },
        'brinjal':{
            'name':'Brinjal',
            'price':'33RS',
            'stock':18

        }
    },
    'fruits':{
        'apple':{
            'name':'Apple',
            'price':'190Rs',
            'stock':21
        },
        'banana':{
            'name':'Banana',
            'price':'55Rs',
            'stock': 24
        },
        'orange':{
            'name':'Orange',
            'price':'65Rs',
            'stock':27
        },
        'mango':{
            'name':'Mango',
            'price':'89Rs',
            'stock':13
        },
        'watermelon':{
            'name':'Watermelon',
            'price':'28Rs',
            'stock':28
        },
        'grapes':{
            'name':'Grapes',
            'price':'150Rs',
            'stock':12
        },
        'papaya':{
            'name':'Papaya',
            'price':'35Rs',
            'stock':19
        },
        'guava':{
            'name':'Guava',
            'price':'89Rs',
            'stock':11
        },
        'pineapple':{
            'name':'Pineapple',
            'price':'35Rs',
            'stock':27
        },
        'pomegranate':{
            'name':'Pomegranate',
            'price':'189Rs',
            'stock':30
        },
        'avocado':{
            'name':'Avocado',
            'price':'260Rs',
            'stock':32
        },
        'dragonfruit':{
            'name':'Dragonfruit',
            'price':'299Rs',
            'stock':31
        
        }
    }
}
# Function to create a new user account
def create_user(name):                   
    print('SIGN-UP')
    print('NOTE : Sorry, Due to the limited knowledge, Now creating an account will be deleted after the program closes. Use the default username and password...')
    print('Creating a user account...')
    username = input('Username : ')
    if username in database['user']:  #This will check if the user had already created account
        print('Same user has been found in our database. Please login...')
        
    else:
        try: 
            password = getpass.getpass(prompt = 'Create Your Account Password : ')   
        except Exception as Error:
            print('Error : ', Error)
        try:
            database['user'][username] = {
                'name': name,                            #Adds Name and password into the database
                'password': password
            }
        except Exception as Error:
            print('Error : ', Error)      
        print('Account created successfully...')

# Function for user sign-in             
def sign_in():                                          
    while True:
        print()
        print()
        print('\t\t\tLOGIN')
        print()
        username = input('Username : ')
        if username == 'admin':
            password1 = getpass.getpass(prompt = 'Password : ')
            if password1 == database['user'][username]['password']:
                print('ADMIN')
                login = True
                admin = True
                return username,login,admin
        elif username in database['user']:                               #Checking given Username is matching with usernames in databse
            password1 = getpass.getpass(prompt = 'Password : ')   
            if password1 == database['user'][username]['password']:    #Checking if the given password is correct with database
                time.sleep(1)
                print('Account logined..')
                print()
                print('Welcome',database['user'][username]['name'])
                username1 = username
                login = True                                           #Intializing the varible as True
                admin = False 
                return username,login,admin                                  #Returning username and login variable 
                break
            else:
                login = False                                          #Intializing the varible as True
                admin = False
                print('Incorrect Password...')
                login_checker(login)   
                return username,login,admin                                  #Returning username and login variable 
        else:  
            time.sleep(1)
            print('Account not Found')
            time.sleep(1)                                              #If the account didnt found on the database then create_user() is called
            print('Creating an account...')
            time.sleep(1)
            print()
            print()
            name  = input('Full name : ')
            create_user(name)

# Function for purchasing items
def buy(l,username):                
    brought_items = []
    while True:
        print()
        item = input('Enter an item : ').lower()                        #User enters the product they need
        if item == 'exit' or item == '0':                               #Exiting the loop
            break
        elif item in brought_items:
            print()                                                     #Checking the cart if the user had already brougtj
            print('Item is already in the cart!!!')
            for i in l:
                if item.title() == i[0]: 
                    print(f'Product : {i[0]}')
                    print(f'Quantity : {i[1]}') 
            print()
            change = input('Do you want to change the quantity ? [yes/no] : ')
            print()                    #Asking the user if they want to change the quantity
            if change == 'yes':
                for i in l:
                    if item.title() == i[0]:
                        if i[0].lower() in database['vegetables']:
                        
                            product,quantity = i   #Unpacking the tuple to change
                            quantity = float(input(f'How much kilo do you need for {database["vegetables"][item]["name"]} : ')) #Asking the change
                            t = product,quantity   #Packing the tuple
                            l.remove(i)            #Removing the existing tuple
                            print(f'Product : {database["vegetables"][item]["name"]}')
                            print(f'Quantity : {database["vegetables"][item]["stock"]}')
                            l.append(t)            #Adding the new tuple into list
                        elif i[0].lower() in database['fruits']:
                            product,quantity = i   #Unpacking the tuple to change
                            quantity = float(input(f'How much kilo do you need for {database["fruits"][item]["name"]} : ')) #Asking the change
                            t = product,quantity   #Packing the tuple
                            l.remove(i)            #Removing the existing tuple
                            print(f'Product : {database["fruits"][item]["name"]}')
                            print(f'Quantity : {database["fruits"][item]["stock"]}')
                            l.append(t)
        elif item == '':
            print('Enter a vaild product')
        else:
            for i in l:
                if item in i[0]:
                    print()
                    print('Item is already added')
            else:
                try:
                    if item.lower() in database['vegetables'] or item.lower() in database['fruits']:          #Checking the product is in database
                        if item.lower() in database['vegetables'] :
                            qut = float(input(f'How much kilo do you need for {database["vegetables"][item]["name"]} : ')) #Asking the quantity
                            if qut < 0:
                                print('The quantity should be more than 0')                    #Checking the quantity is more than 0
                                buy(l,username)
                                break
                            if qut > database['vegetables'][item]['stock']:                    #Checking the given quantity is less than the stock
                                print(f'The quantity should be less than the TOTAL STOCK, Remaining Stock : {database["vegetables"][item]["stock"]}')
                                buy(l,username)
                                break

                            brought_items.append(item)                                          #Adding the item into the cart
                            items = (database['vegetables'][item]['name'],qut)
                            l.append(items)

                            database['vegetables'][item]['stock'] = database['vegetables'][item]['stock'] - qut     

                            print(f"Remaining Stocks = {database['vegetables'][item]['stock']}")

                            if database['vegetables'][item]['stock'] == 0:                   
                                del database['vegetables'][item]

                            
                        elif item.lower() in database['fruits']:
                            qut = float(input(f'How much kilo do you need for {database["fruits"][item]["name"]} : '))
                            if qut < 0:
                                print('The quantity should be more than 0')                    #Checking the quantity is more than 0
                                buy(l,username)
                                break
                            if qut > database['fruits'][item]['stock']:                    #Checking the given quantity is less than the stock
                                print(f'The quantity should be less than the TOTAL STOCK, Remaining Stock : {database["fruits"][item]["stock"]}')
                                buy(l,username)
                                break

                            brought_items.append(item)                                          #Adding the item into the cart
                            items = (database['fruits'][item]['name'],qut)
                            l.append(items)

                            database['fruits'][item]['stock'] = database['fruits'][item]['stock'] - qut     

                            print(f"Remaining Stocks = {database['fruits'][item]['stock']}")

                            if database['fruits'][item]['stock'] == 0:                   
                                del database['fruits'][item]
                    else:
                        print('Item not found')
                       
                except ValueError:                                                    #Exception handling
                    print('Please enter a valid value...')
    
    if username in user_buy:
        existing_items = user_buy[username]
        l1 = existing_items + l
        user_buy[username] = l1
        addInfo(user_buy)
        return user_buy,l
        
    else:
        user_buy[username] = l
        addInfo(user_buy)
        return user_buy,l
        
             

#Function for listing the items
def list1(database):                                                                   
    vegetable_data = database.get('vegetables')
    fruits_data = database.get('fruits')

    if not vegetable_data:
        print("No vegetable data found!")                                                    #Checking if the database is empty or not
        return
    print()
    print("------------------------------------------\t\t -----------------------------------------")
    print("|   Vegetable   |     Price     | Stock  |\t\t|    Fruits     |     Price     | Stock  |")
    print("------------------------------------------\t\t -----------------------------------------")

    veg_keys = list(database['vegetables'].keys())
 
    fru_keys = list(database['fruits'].keys())
    
    for i, j in zip(veg_keys,fru_keys):
        veg_name = database['vegetables'][i]['name'].ljust(15)
        veg_price = database['vegetables'][i]['price'].ljust(15)
        veg_stock = str(database['vegetables'][i]['stock']).ljust(8)

        fruit_name = database['fruits'][j]['name'].ljust(15)
        fruit_price = database['fruits'][j]['price'].ljust(15)
        fruit_stock = str(database['fruits'][j]['stock']).ljust(8)

        print(f'|{veg_name}|{veg_price}|{veg_stock}|\t\t|{fruit_name}|{fruit_price}|{fruit_stock}|')
    print("------------------------------------------\t\t -----------------------------------------")

def recipt(username,brought_items):                                                   #Function for printing the recipt
    confirm =  input('Anything else ? : ').lower()                    #Asking the user if they want to buy anything else
    if confirm == 'yes':
        l =  user_buy.get(username)
        userbuy, brought_items = buy(l,username)
    total_amount = 0  # Initialize the total amount variable

    print()
    print('=' * 70)
    print('RECEIPT'.center(70))
    print('=' * 70)
    time2 = time.asctime()                                              #Getting the current time

    print('Name : ',database['user'][username]['name'],'\t\t\t','Date : ',time2)
    print('=' * 70)
 
    print(''.ljust(8),'ITEM'.ljust(19),'RATE'.ljust(14),'QUANTITY'.ljust(17),'TOTAL')
    print('=' * 70)
    
    for i in  brought_items:
        product_name, quantity = i
        price_per_kilo = 0

        # Check if the product is a vegetable or a fruit
        if product_name.lower() in database['vegetables']:
            price_per_kilo = float(database['vegetables'][product_name.lower()]['price'][:-2])  # Extract price per kilo
        elif product_name.lower() in database['fruits']:
            price_per_kilo = float(database['fruits'][product_name.lower()]['price'][:-2])  # Extract price per kilo

        total_price = price_per_kilo * quantity
        total_amount += total_price

        print(product_name.ljust(20) ,'|'.ljust(3),str(price_per_kilo).ljust(5), " RS/kg".ljust(8) ,'|'.ljust(4),str(quantity).ljust(3) ," kg".ljust(6) ,'|'.ljust(3) ,str(total_price).ljust(5) , " RS".ljust(20))
          
    print()
    print('=' * 70)
    print('Total Amount :',total_amount,' RS')

def login_checker(login):
    if login != True:
        sign_in()
def adminf():
    print('ADMIN PANEL')
    print('1. Change the rate of the product')
    print('2. Change the stock of the product')
    print('3. ORDERS')
    while True:
        choice = int(input('Enter the choice : '))
        if choice == 1:
            prodName = input('Product Name : ').lower()
            if prodName in database['vegetables'] or prodName in database['fruits']:
                if prodName in database['vegetables']:
                    for i in database['vegetables']:
                        if i == prodName:
                            rate =  input('Enter the revised rate : ')
                            database['vegetables'][prodName]['price'] = rate+'RS'
                            print('Rate updated successfully...')
                            print(f'PRODUCT : {database["vegetables"][prodName]["name"]}')
                            print(f'RATE : {database["vegetables"][prodName]["price"]}')
                elif prodName in database['fruits']:
                    for i in database['fruits']:
                        if i == prodName:
                            rate =  input('Enter the revised rate : ')
                            database['fruits'][prodName]['price'] = rate+'RS'
                            print('Rate updated successfully...')
                            print(f'PRODUCT : {database["fruits"][prodName]["name"]}')
                            print(f'RATE : {database["fruits"][prodName]["price"]}')
                else:
                    print('404 Item Not Found')
            else:
                print('404 Item Not Found')
        elif choice == 2:
            prodName = input('Product Name : ').lower()
            if prodName in database['vegetables'] or prodName in database['fruits']:
                if prodName in database['vegetables']:
                    for i in database['vegetables']:
                        if i == prodName:
                            stock =  input('Enter the revised rate : ')
                            database['vegetables'][prodName]['stock'] = stock
                            print('Rate updated successfully..')
                            print(f'PRODUCT : {database["vegetables"][prodName]["name"]}')
                            print(f'STOCK : {database["vegetables"][prodName]["stock"]}')
                elif prodName in database['fruits']:
                    for i in database['fruits']:
                        if i == prodName:
                            stock =  input('Enter the revised rate : ')
                            database['fruits'][prodName]['stock'] = stock
                            print('Rate updated successfully..')
                            print(f'PRODUCT : {database["fruits"][prodName]["name"]}')
                            print(f'STOCK : {database["fruits"][prodName]["stock"]}')
                else:
                    print('404 Item Not Found')
            
            else:
                print('404 Item Not Found')
        elif choice ==3:
            print('ORDERS')
            user_buy1 = getInfo('user_buy')
            print(user_buy1)
        elif choice == 0 :
            break
        else:
            print('Invalid Choice')
def addInfo(var):
    for name, value in globals().items():  # Use locals() for local variables
        if value is var:
            
            var_name = name
    f = open(Path('data.txt'),'w')
    f.write(f'{var_name} = {var}\n')
    f.close()
def getInfo(var):
    
    with open(Path('data.txt'), 'r') as file:
    # Read each line in the file
        for line in file:
            # Check if the line contains the variable you want
            if line.startswith(var):
                # Split the line at '=' to get the value part
                variable_value = line.split('=')[-1].strip()
                # Print the variable value
                return variable_value
                  # Stop reading after finding the variable
            else:
                print('404 Item Not Found')
                

print()
print('='*55)
print()
print('  / ____| |  | |/ __ \|  __ \_   _|  ____\ \   / /')     
print(' | (___ | |__| | |  | | |__) || | | |__   \ \_/ / ')    
print('  \___ \|  __  | |  | |  ___/ | | |  __|   \   /  ')     
print('  ____) | |  | | |__| | |    _| |_| |       | |   ')
print(' |_____/|_|  |_|\____/|_|   |_____|_|       |_|   ')
print()
print('='*55)
if not getInfo('user_buy'):
    user_buy={}
else:
    user_buy =  eval(getInfo('user_buy'))


time.sleep(1)
n=0
def main():
    username = None
    while True:
        time.sleep(1)
        username,login, admin = sign_in() 
        time.sleep(1)
        if admin == False :

            list1(database)
            print()
            buy_accept =  input('Wanna buy something from our store ??? [yes/no] : ').lower()   #Asking the user if they want to buy anything..reconfirming
            if buy_accept == 'yes':
                time.sleep(1)
                l = []
                print()
                print('NOTE : Type  "0" or "exit" after finishing adding the products')
                userbuy, brought_items = buy(l,username)
                if user_buy[username] == []:
                    pass
                else:
                    recipt(username,brought_items)
            else:
                time.sleep(1)
                print('Thank you for coming')
                time.sleep(5)
            break
        elif admin == True:
            adminf()
            


if __name__ == "__main__":
    main()
    while True:
        time.sleep(2)
        choice = input("Press 'q' to quit or any other key to continue shopping : ")  #Asking the user if they want to continue shopping
        if choice.lower() == 'q':
            print('Thank you for coming\nVisit again!!!')
            print("Exiting the program...")
            break
        else:
            print('NEXT CUSTOMER PLEASE...')
            time.sleep(2)
            main()
