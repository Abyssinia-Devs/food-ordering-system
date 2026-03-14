owner_password='sam123'
import pwinput
from tabulate import tabulate
from rich.console import Console
from rich.table import Table
from collections import defaultdict
from typing import Any, Dict, List
import datetime


#from helper_func import read_input, read_num, read_range, display_food_category, display_item_by_category, display_menu,select_food_category
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
MenuItem = Dict[str, Any]
MenuCategory = Dict[str, Any]
MenuType = List[MenuCategory]


console = Console()  # Create a Rich Console object to print styled text, tables, and other rich content to the terminal  
now = datetime.datetime.now() # get current date and time

def food_sales_(orders)->dict:
    food_sales_price = defaultdict(int)
    for order in orders:
        for item in order["items"]:
            food_sales_price[item["name"]] += (item["price"]*item['stock_quantity'])
    return (food_sales_price)


def bar_graph(orders)->None:
    if not orders:
        console.print("[red] There is no order [/red]")
    food_sales_total_price=food_sales_(orders)
    max_sales_total=max(food_sales_total_price.values())
    bar_width=20
    table = Table(title="Food Sales", title_style="bold purple italic underline")
    table.add_column("Food", header_style="bold cyan")
    table.add_column("Sales Price", justify="right",header_style='bold blue')
    table.add_column("Graph",header_style='bold green')
    
    for food,sales_total in food_sales_total_price.items():
        if not max_sales_total:
            console.print("There is no max values")
            return
        bar_length = int((sales_total / max_sales_total) * bar_width) 
        bar ="◉" * bar_length #"█" 
        table.add_row(food, str(sales_total), f"[green]{bar}[/green]")
    console.print(table)
    
    
def owner_login()->bool:
    trials=3
    while trials>0:
        passkey = pwinput.pwinput(prompt="Enter password: ", mask="*").strip()
            
        if passkey==owner_password:
            return True
        
        trials-=1
        console.print(f"Incorrect Password! [bold red]{trials}[/bold red] left")

    

def read_int(prompt, min_val=None, max_val=None)->int:
    while True:
        try:
            value = int(input(prompt))
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                console.print(f"Enter a number between {min_val} and {max_val}.")
                continue
            return value
        except ValueError:
            console.print("[red3]Enter a valid number.[/red3]")
            
            
def read_float(prompt, min_val=None)->float:
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                console.print(f"Enter a value >= {min_val}.")
                continue
            return value
        except ValueError:
            console.print(f"[red3]Enter a valid number .[/red3]")


def display_food_category(menu:MenuType)->None:
    print("\nMenu Categories")
    for index, category in enumerate(menu, 1):
        console.print(f"{index}. {category['category'].upper()}")




class Owner:
    def __init__(self, menu: List[Dict], orders: List[Dict]):
        self.menu = menu
        self.orders = orders
    
    
    def status(self,status)->None:
        print("-"*10)
        print(f"1.To {status} food.")
        print("0.To Exit.")
        print("-"*10) 
        
    
    def add_food(self):
        while True:
            self.status("Add")
            
            choice=read_int(">", 0, 1)
            match choice:
                case 0:
                    break
                case 1:
                    display_food_category(self.menu)
                    choice = read_int("Select category to add food :", 1, len(self.menu)) - 1
                    
                    category_block=self.menu[choice]
                    items=category_block["items"]
                    name = input("Enter food name: ").strip().title()
                    
                    for item in (items):
                        if item['name'].lower() ==name.lower():
                            console.print(f"{item['name']} already exist.")
                            return 
                    
                    price=read_float("Price: ",0)
                    stock_quantity=read_int("Stock: ",1)
                    items.append({"name":name,"price":price,'stock_quantity':stock_quantity})
                    console.print(f"[bold green]{name}[/bold green] added sucessfully✅")
                    
                    

    def display_menu(self):

        for cat_no, category_block in enumerate(self.menu,start=1):
            category=category_block['category']
            items=category_block['items']
            console.print(f"\n[bold orange1]Category {cat_no}. {category.upper()}[/bold orange1]")
            rows=[]
            for item_no,item in enumerate(items,start= 1):
               rows.append(
                   [item_no,item['name'],item["price"],item["stock_quantity"]]
               ) 
            
            print(
                tabulate(rows,headers=["No","Name","Price","Stock"],tablefmt="fancy_grid")
            )
            
            
        
    def display_item_by_category(self,choice_category):
        
        
        categoryblock=self.menu[choice_category]
        items=categoryblock["items"]
        
        rows=[]
        if len(items)<=0:
            print("No Food.")
            return
        for item_no,item in enumerate(items,start=1):
            rows.append(
                [item_no,item["name"],item['price'],item['stock_quantity']]
            )
        print(
            tabulate(
                rows,headers=["No","Name","Price","Stock"],tablefmt="fancy_grid"
            )
        )  
        
        
    def delete_food(self):
        while True:
            self.status('Delete')
            choice=read_int(" >",0,1)
            match choice:
                case 0:
                    return 
                case 1:
                    display_food_category(self.menu)
                    choice_category=read_int(">",1,len(self.menu))-1
                    categoryblock=self.menu[choice_category]
                    items=categoryblock["items"]

                    if not items:
                        console.print(f"Out of [bold blue]{categoryblock['category']}[/bold blue]")
                        return
                    self.display_item_by_category(choice_category)
                    
                    foods_nums=read_int("Enter number of foods to delete",1,len(items))
                    indexes=[]
                    for food_num in range(1,foods_nums+1):
                        food_idx = read_int(f"{food_num}.Select the index  of food to delete: ", 1, len(items)) - 1
                        indexes.append(food_idx)
                    
                    for index in sorted(set(indexes),reverse=True):
                        removed=items.pop(index)
                        console.print(f"[bold red]{removed['name']} deleted.[/bold red]")
                        
                                    
    def update_price(self):
        while True:
            self.status("Update_price")
            choice=read_int('>',0,1)
            
            match choice:
                case 0:
                    break
                case 1:
                    display_food_category(self.menu)
                    choice_category=read_int(">",1,len(self.menu))-1
                    categoryblock=self.menu[choice_category]
                    items=categoryblock["items"]

                    if not items:
                        console.print(f"Out of [bold blue]{categoryblock['category']}[/bold blue]")
                        return
                    self.display_item_by_category(choice_category)
                    food_idx=read_int("Enter the index of the food: ",1,len(items))-1
                    old_price=items[food_idx]['price']
                    new_price=read_float("Enter the price: ",10)
                    items[food_idx]['price']=new_price
                    console.print(
                                f"[orange1]{old_price}[/orange1] price of {items[food_idx]['name']} updated to [bold green]{new_price}[/bold green] birr"
                                )
                    

    
    
    def update_stock(self):
        while True:
            self.status("Update_stock")
            choice=read_int('>',0,1)
            
            match choice:
                case 0:
                    break
                case 1:
                    display_food_category(self.menu)
                    choice_category=read_int(">",1,len(self.menu))-1
                    categoryblock=self.menu[choice_category]
                    items=categoryblock["items"]

                    if not items:
                        console.print(f"Out of [bold blue]{categoryblock['category']}[/bold blue]")
                        return
                    self.display_item_by_category(choice_category)
                    food_idx=read_int("Enter the index of the food: ",1,len(items))-1
                    old_stock=items[food_idx]['stock_quantity']
                    new_stock=read_int("Enter the new_stock: ",10)
                    items[food_idx]['stock_quantity']=new_stock
                    console.print(f"[orange1]{old_stock}[/orange1]  value of {items[food_idx]['name']} updated to [bold green]{new_stock}[/bold green] ")
    
    
    
    def view_orders(self):
        if not self.orders:
            console.print("[bold red]There is no order.[/bold red]")
            return
        rows=[]
        for food_index,order in enumerate(self.orders):
            rows.append([order["order_id"],order["name"],order["phone"],order["total"],order["paid"],order["status"]])
            #if not order['items']:
                #print(f"There is no item in {order['items']}")
            console.print(tabulate(
            [rows[food_index]],headers=["order_id",'Customer name',"Phone_No","Total_birr","Paid","Status"],tablefmt="fancy_grid"
            ))
            
            row_item=[[item["name"],item['price'],item['stock_quantity'],item['sub_price']]for item in order['items']]
            console.print("[blue]___________________order_items__________________________________________[/blue]")
            console.print(tabulate(
            row_item,headers=["Name","Price","Quantity","Sub_total birr"],tablefmt="fancy_grid"
            ))
            console.print("**"*35)
             


    def sales_summary(self):
        if not self.orders:
            console.print("[bold red]There is no order.[/bold red]")
            return
        bar_graph(self.orders)
        summary={
            'total_sales':0,
            'total_orders':len(self.orders),
            'average_sales':0
        }
        if not self.orders:
            console.print("[red3]There is no order.[/red3]")
            return
        
        for order in self.orders:
            summary ['total_sales']+= order['total']
            
        try:
            summary["average_sales"]= summary["total_sales"]/summary["total_orders"]
        
        except ZeroDivisionError:
            console.print(" [red]Error there is no order[/red]")
            return

        table = Table(title="Summary",title_style="bold green",style="bold blue")

        table.add_column("Total Sales", style="cyan", justify="center")
        
        table.add_column("Total orders", style="green")
        table.add_column("Average Sales", header_style="bold red",style="yellow")

        table.add_row(f"{summary['total_sales']}", f"{summary['total_orders']}", f"{summary['average_sales']}")
        console.print(table)
        
        console.print(now)  
            
    
    def owner_menu(self):
        console.print("[bold green]========================================\n||       GS FOOD ORDERING PLATFORM     ||\n========================================[/bold green]")
        while True:
            console.print("\n[bold blue]OWNER MENU[/bold blue]")
            console.print("1. Add Food\n2. Delete Food\n3. Update Price\n4. Update Stock\n5. View Orders\n6. Sales Summary\n7. Display menu \n0.[bold red]log Out[/bold red]")
            choice=read_int('Enter your choice>',0,7)
            
            if choice==0: break
            elif choice==1: self.add_food()
            elif choice==2: self.delete_food()
            elif choice==3: self.update_price()
            elif choice==4: self.update_stock()
            elif choice==5: self.view_orders()
            elif choice==6: self.sales_summary()
            elif choice==7: self.display_menu()

        
        
def owner_flow(menu, orders):
    
    console.print("[bold green]=== OWNER LOGIN ===[/bold green]")
    if owner_login():
        console.print("[bold green] 🗝️🔓 Welcome. Owner [/bold green]")
        Owner(menu, orders).owner_menu()
    
    console.print(now) 
    console.print("[bold red]locked🔒[/bold red]")








