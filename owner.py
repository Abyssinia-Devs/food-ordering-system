owner_pssword='sam123'
food_menu=[]
one_food={}
class Status:
     j=1

def owner_login():
    passkey=(input('Enter the password:'))
    if passkey==owner_pssword:
        return True
    else:
        return False

def owner_menu():
    
    def list_menu():
        
        print('1.Add Food')
        print('2.Delete Food')
        print('3.Update Price')
        print('4.Update stock')
        print('5.View orders')
        print('6.View sales summary')
        print('0.EXIT')

    while True:
        list_menu()
        choice=int(input('Enter your choice:'))
        if choice==1:
            add_food()
      
        elif choice==2:
            delete_food()
        
        elif choice ==3:
            update_food_price()
       
        elif choice ==4:
            update_food_stock()
        
        elif choice==5:
            view_orders()
      
        elif choice==6:
            view_sales_summary()
        
        elif choice==0:
            break
        else:
            print('please enter only from the choice.')

def add_food():
   
    def show():
        print('1.To Add:')
        print('0.To Exit:')
        choice=int (input('Enter your choice:'))
        return choice
    choice=show()
    

    def addFoodto_Menu():
            food_toadd=int(input('Enter the number of food you want to add:'))
            for i in range(1,food_toadd +1):

                food_name=(input(f"{i}.Enter Food Name:"))
                price=float(input(f"  -Price:$"))
                available_stock=int(input('  -Available stock:'))
                #one_food[str(i),'price','available stock']= food_name,price,available_stock
                #one_food.update({'str({i})':food_name,'price':price,'available_stock':available_stock})
                one_food={
                    f'{Status.j}':food_name,
                    'price':price,
                    'available stock':available_stock
                }
                Status.j+=1
                food_menu.append(one_food)
                print('added.')
            again_choice=int(input('Add again 1 ,see what you added 2,not 0:'))
            if again_choice==1:
                addFoodto_Menu()
            
            elif again_choice==2:
                show_add()
                    
            elif again_choice==0:
                owner_menu()
            else:
                print('Please only enter from the choice only.')
    def show_add():
        for i in food_menu:
            print(i)
   
    while True:

        if choice==1:
            addFoodto_Menu()
            break
            
           
        elif choice==0:
            owner_menu()
        else:
            print('Please only enter from the choice only.')
            



def delete_food():
    pass


def update_food_price():
    pass


def update_food_stock():
    pass


def view_orders():
    pass

def view_sales_summary():
    pass


def owner_flow():
    
    print('------------------------------------')
    print("1.Enter password")
    print('0.Exit')
    print('------------------------------------')
    
    
    while True:
        choice=int(input('Choice:'))
        if choice==1:
            Authentication=owner_login()
            if Authentication==True:
                menu=owner_menu()
                
            else:
                print('Incorrect password.')
                
        elif choice==0:
            break
owner_flow()
    