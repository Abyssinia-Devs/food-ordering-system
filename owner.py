owner_password='sam123'
from tabulate import tabulate
from helper_func import read_input, read_num, read_range, display_food_category, display_item_by_category, display_menu,select_food_category
# This program simulates an owner management system for a restaurant.
# The owner can login with a password and then:
# - Add new food items to categories (main meal, fast food, drinks)
# - Delete existing food items
# - Update the price of food items
# - Update the stock quantity of food items
# - View all customer orders
# - View a sales summary including total and average sales
# The program uses nested menus and input validation to interact with the owner.

# ==================== owner auth ======================
def owner_login():
    passkey =read_input("Enter your password: ")
    if passkey==owner_password:
        return True
    else:
        return False

def owner_menu():
    print('1.Add Food')
    print('2.Delete Food')
    print('3.Update Price')
    print('4.Update stock')
    print('5.View orders')
    print('6.View sales summary')
    print('0.EXIT')
class Menu:
    def add_food(self, food_menu):
        while True:

            print("-"*10)
            print("1.To add food.")
            print("0.To Exit.")
            print("-"*10)
            
            choice=read_range(">", 0, 1)
            if choice==0:
                break
            
            elif choice==1:
                display_food_category(food_menu)
                category=select_food_category("Select food category: ", food_menu)

                    
            #     except ValueError:
            #         print("Enter numbers only.")
            #         continue
            #     if category==0:
            #         break
                
            #     elif category in [1,2,3]:
            #         items=food_menu[category-1]['items']    
                
            #         print(f"-----------Current--{food_menu[category-1]['category']}------------------------")
            #         current_food_menu_list(items)

            #         try:
            #             foodsto_add=int(input('Enter the number of foods to be added: '))
                    
            #         except ValueError:
            #             print('Enter numbers onlyl.')
            #             continue
                        
            #             for k in range(0,(foodsto_add)):
                        
            #                 exist=False
            #                 name = input("Name: ").strip().replace(" ", "")
                            
            #                 try:
                                
            #                     price=float(input('Price: '))
            #                     stock=int(input("Available_Sock: "))
                            
            #                 except ValueError:
                                
            #                     print("Error Enter numbers only.")
            #                     continue
                        
            #                 for j in range(len(items)):
                            
            #                     if name.lower() == items[j]['name'].lower():
                                
            #                         exist=True
            #                         break
                            
            #                 if not exist:
            #                     if (price >0) and (stock >=0) and name:
                        
            #                         items.append({'name':name,'price':price,'stock_quantity':stock})
            #                         print(f"✅{name} added successfully!")
                                    
            #                     else:
            #                         print("Invalid.")
                            
            #                 elif exist:
            #                     print(f"{name} already exist!❌")
                        
            #                 print(f"-----------Updated {food_menu[category-1]['category']}------------------------")
            #                 current_food_menu_list(items)
                    
            #         else:
            #             print("Invalid.")
            
            # except ValueError:
                
            #     print('Error enter numbers only.')        

                
    def delete_food(self, food_menu):
        
        def current_food_menu_list(items):
            
            if len(items)>0:
                for i in range(len(items)):

                    print(f"{i+1}.Name--{items[i]['name']}")
                    print(f"Price--{items[i]['price']}")
                    print(f"Stock--{items[i]['stock_quantity']}")
                    print("-"*35)
            else:
                print("NO food.")
                
        while True:

            print("-"*10)
            print("1.To delete food.")
            print("0.To Exit.")
            print("-"*10)
            
            try:
                choice=int(input("Enter your choice: "))
                
            except ValueError:
                print("Enter from the given numbers only.")
                continue
            
            if choice==0:
                break
            
            elif choice==1:
                
                while True:
                    print("1.For Main_meal ")
                    print("2.For Fast_food")
                    print("3.For Drinks")
                    print("0.Back to main")
                
                    try:
                        choice_category=int(input("Enter your choice: "))
                
                    except ValueError :
                        print("Enter from the given numbers only.")
                        continue
                    
                    if choice_category==0:
                        break
                    
                    elif choice_category in (1,2,3):
                        items=food_menu[choice_category-1]['items']   
                        print(f"----------- Current {food_menu[choice_category-1]['category']}------------------------")
                        current_food_menu_list(items)
                    
                            
                        try:
                            foods_to_delete=int(input('Enter the number of foods to be deleted.'))
                        
                        except ValueError:
                            print('Enter numbers only.')
                            continue
                        
                        indexes = []
                        
                        if (foods_to_delete) <= len(items):
                            for k in range(1,(foods_to_delete)+1):
                        
                                #exist=False
                                try:
                                    index=int(input('Index of food '))
                                
                                except ValueError:
                                    print("Enter numbers only.")
                                    continue
                                
                                if 1<= index <= len(items):
                                    indexes.append(index-1)
                                    
                                else:
                                    print("Invalid index")
                                
                            for index in sorted(indexes, reverse=True):
                                
                                deleted_food = items.pop(index)
                                print(f"{deleted_food['name']} deleted.")
                            
                            print(f"-----------After deleted---{food_menu[choice_category-1]['category']}------------------------")
                            current_food_menu_list(items)
                            
                            print("-"*40)    
                                
                        else:
                            print(f" Out of food -->  number of current foods are {len(items)}")
                    
                    else:
                        print("Invalid.")
    

    def update_food_price(self, food_menu):
        
        def current_food_menu_list(choice_category):
            
            items = food_menu[choice_category-1]['items']
            
            if len(items) > 0:
                
                for i, item in enumerate(items, start=1):
                    
                    print(f"{i}. Name--{item['name']}")
                    print(f"Price--{item['price']}")
                    print(f"Stock--{item['stock_quantity']}")
                    print("-"*35)
            else:
                print("NO food.")

        while True:
            print("-"*10)
            print("1.Update the price.")
            print("0.To Exit.")
            print("-"*10)

            try:
                choice = int(input("Enter your choice: "))
                
            except ValueError:
                print("Enter numbers only.")
                continue

            if choice == 0:
                break
            
            elif choice == 1:
                
                while True:
                    print("1. Main_meal")
                    print("2. Fast_food")
                    print("3. Drinks")
                    print("0.Back to main")

                    try:
                        category = int(input("Choose a category: "))
                        
                    except ValueError:
                        print("Enter numbers only.")
                        continue

                    if category == 0:
                        break
                    
                    elif category in [1,2,3]:
                        items = food_menu[category-1]['items']
                        print(f"-----------Current {food_menu[category-1]['category']}------------------------")
                        current_food_menu_list(category)

                        try:
                            food_index = int(input('Enter the index of food you want to update the price: '))
                            new_price = float(input("Enter the new price: "))
                        
                        except ValueError:
                            print("Enter numbers only.")
                            continue

                        if 1 <= food_index <= len(items) and new_price > 0:
                        
                            old_price = items[food_index-1]['price']
                            items[food_index-1]['price'] = new_price
                            print(f"${old_price} updated to ${new_price}")
                        
                        else:
                            print(f"Invalid index. Current food index is 1 to {len(items)}.")

                        print("-----------After updated price------------------------")
                        current_food_menu_list(category)
                    else:
                        print("Invalid.")
            
    def update_food_stock(self, food_menu):
        
        def current_food_menu_list(choice_category):
            items = food_menu[choice_category-1]['items']
            if len(items)>0:
                
                for i in range(len(items)):

                    print(f"{i+1}.Name--{items[i]['name']}")
                    print(f"Price--{items[i]['price']}")
                    print(f"Stock--{items[i]['stock_quantity']}")
                    print("-"*35)
            else:
                print("NO food.")
        
        while True:

            print("-"*10)
            print("1.Update the stock_quantity.")
            print("0.To Exit.")
            print("-"*10)
                
            try:
                choice=int(input("Enter your choice: "))
                
            except ValueError:
                print("Enter from the given numbers only.")
                continue
            
            if choice==0:
                break
            
            elif choice==1:
                
                while True:
                    
                        print("1.For Main_meal ")
                        print("2.For Fast_food")
                        print("3.For Drinks")
                        print("0.Back to main")
                
                        try:
                            choice_category=int(input("Enter your choice: "))
                
                        except ValueError :
                            print("Enter from the given numbers only.")
                            continue
                        
                        if choice_category==0:
                            break
                    
                        elif choice_category in (1,2,3):
                            items = food_menu[choice_category-1]['items']
                            print(f"--------------{food_menu[choice_category-1]['category']}---------------------")
                        
                            current_food_menu_list(choice_category)
                        
                            try:
                                food_stock_update=int(input('Enter the index of food you want to update the stock Quantity.'))
                                new_stock=int(input("Enter the new stock: "))
                            
                            except ValueError:
                            
                                print('Enter numbers only.')
                                continue
                        
                            if (1<=food_stock_update <=len(items)) and (new_stock >=0):
                            
                                old_stock = items[food_stock_update-1]['stock_quantity']
                                items[food_stock_update-1]['stock_quantity']=new_stock
                                print(f"{old_stock} updated to {new_stock}")
                        
                            else:
                            
                                print(f"{food_stock_update}- Invalid index-- your current food index is up t0 1--{len(items)}.")
                        
                                print(f"-----------Current {food_menu[choice_category-1]['category']}------------------------")
                            
                                current_food_menu_list(choice_category)
                                
                        else:
                            print("Invalid.")
                        
                    

# [{'order_id': 'ORD-525', 'name': 'mik', 'phone': '0987654321', 'items': [{'name': 'tea', 'price': 65, 'stock_quantity': 3, 'sub_price': 195}], 'status': 'pending', 'total_price': 195.0}]
def view_orders(orders):

    if len(orders)==0:

        print(' THERE IS NO ORDER YET.')
        return
    print("*" *30)
    for order in orders:

        print(f"order_id-{order['order_id']}")
        print(f"Customer_Name-{order['name']}")
        print(f"Phone-No-{order['phone']}")
        print("Items:")
        rows=[]
        for role_no, item in enumerate(order['items'],1):
            rows.append(
                [role_no, item["name"], item["stock_quantity"]]
            )
        print(tabulate(rows,  headers=["No", "Name","Quantity"], tablefmt="fancy_grid"))
        print(f"Total${order['total_price']}")
        print(f"Status-{order['status']}")
        print("-"*30)
    print("*" *30)


def view_sales_summary(orders):
    
    summary={
        'total_sales':0,
        'total_orders':len(orders),
        'average_sales':0
    }
    for order in orders:
        summary['total_sales']+=order['total']
    try:
        summary['average_sales']=summary['total_sales']/summary['total_orders']
    except ZeroDivisionError:
        print('There is no order')
        
    
    print('________________________SUMARRY____________________________')
    print("-"*30)
    print(f"{'Items':<15} | {'Values':>10}")
    print("-"*30)
    for Item,Value in summary.items():
        print(f"{Item:<15} | {Value:>10}")
    print("-"*30)
    print("__"*29)


def owner_flow(food_menu,orders):
    menu = Menu()
    while True:
        print('------------------------------------')
        print("1. Enter password")
        print('0. Exit')
        print('------------------------------------')

        choice = read_range(">",0,1)
        if choice == 0:
            print("Exiting Owner Control Panel.")
            break
        if choice == 1:
            authentication = owner_login()
            if authentication:
                print("Welcome!")
            else:
                print('Incorrect password.')
                continue

            while True:
                owner_menu()
                choice=read_range(">", 0, 6)
                if choice==1:
                    menu.add_food(food_menu)
                elif choice==2:
                    menu.delete_food(food_menu)
    
                elif choice ==3:
                    menu.update_food_price(food_menu)
    
                elif choice ==4:
                    menu.update_food_stock(food_menu)
                elif choice==5:
                    view_orders(orders)
    
                elif choice==6:
                    view_sales_summary(orders)
                elif choice==0:
                    break
  

    