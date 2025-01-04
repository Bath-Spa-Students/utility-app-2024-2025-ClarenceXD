from prettytable import PrettyTable                                                 #imports prettytable-3.12.0
snacks = PrettyTable()
drinks = PrettyTable()
#dict to hold items name,cost, and stock
A00 = {                                                                             
  "A01" : {
    "name" : "Potato Chips",
    "stock" : 3,
    "cost" : 10
  },
  "A02" : {
    "name" : "Crackers",
    "stock" : 6,
    "cost" : 10
  },
  "A03" : {
    "name" : "peanuts",
    "stock" : 8,
    "cost" : 15
  },
  "A04" : {
    "name" : "Pretzels (salted)",
    "stock" : 2,
    "cost" : 20
  },
  "A05" : {
    "name" : "Trail Mix",
    "stock" : 4,
    "cost" : 20
  },
  "B01" : {
    "name" : "Protein Bars",
    "stock" : 10,
    "cost" : 5
  },
  "B02" : {
    "name" : "Cookies",
    "stock" : 2,
    "cost" : 10
  },
  "B03" : {
    "name" : "Muffins (3)",
    "stock" : 4,
    "cost" : 20
  },
  "B04" : {
    "name" : "Chocolate-Covered Almonds",
    "stock" : 2,
    "cost" : 25
  },
  "B05" : {
    "name" : "Gum Ball",
    "stock" : 4,
    "cost" : 10
  },
  "C01" : {
    "name" : "Mtn Dew (250ml)",
    "stock" : 4,
    "cost" : 15
  },
  "C02" : {
    "name" : "Ice Tea (250ml)",
    "stock" : 2,
    "cost" : 25
  },
  "C03" : {
    "name" : "Iced Coffee (200ml)",
    "stock" : 7,
    "cost" : 25
  },
  "C04" : {
    "name" : "Energy Drink (250ml)",
    "stock" : 7,
    "cost" : 20
  },
  "C05" : {
    "name" : "Lemonade (250ml)",
    "stock" : 7,
    "cost" : 20
  },
  "D01" : {
    "name" : "Hot Chocolate (200ml)",
    "stock" : 2,
    "cost" : 20
  },
  "D02" : {
    "name" : "Coffee (200ml)",
    "stock" : 3,
    "cost" : 25
  },
  "D03" : {
    "name" : "Tea (200ml)",
    "stock" : 2,
    "cost" : 25
  },
  "D04" : {
    "name" : "Black Tea (200ml)",
    "stock" : 3,
    "cost" : 20
  },
  "D05" : {
    "name" : "Espresso (200ml)",
    "stock" : 3,
    "cost" : 30
  }
}
#Creates the menu with current values
def menu():                                                                           
  snacks.field_names = ["--Code--","--Snacks--","--Cost--","--Stock--"]
  drinks.field_names = ["--Code--","--Drinks--","--Cost--","--Stock--"]
  for a in A00:
      if a[0:1] == ("A") or a[0:1] == ("B") :                                     #snacks
        snacks.add_row ([(a),(A00[(a)]['name']),f"{A00[(a)]['cost']}$",(A00[(a)]['stock'])])
        if a == ("A05"):
          snacks.add_row (["---","--------------------------","----------","----------"])
      if a[0:1] == ("C") or a[0:1] == ("D") :                                     #drinks
        drinks.add_row ([(a),(A00[(a)]['name']),f"{A00[(a)]['cost']}$",(A00[(a)]['stock'])])
        if a == ("C05"):
          drinks.add_row (["---","--------------------------","----------","----------"])
#prints created table then clears table to update
def display_menu():
  menu()
  print(snacks)
  print("|                                                                 |")
  print("|                                                                 |")
  print(drinks)
  snacks.clear()
  drinks.clear()

print("""
██╗   ██╗███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
██║   ██║██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██║   ██║█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
 ╚████╔╝ ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
                                                                                                                     """)
display_menu()
user_money = int(input("Insert Money (avg price per item is 25$): "))
#using loop to allow user to buy multiple items
while True:                                                                         
    user_input = str(input("-Menu(1)--Exit(0)----Enter Item Code: ").capitalize())      
    #exit                            
    if user_input == "0":
        print(f"\n\n⚠️  Thank you for your purchase ヾ(•ω•`)o! Dispensing your change: {user_money}$. ⚠️\n")                                                 
        exit()
    #display menu
    elif user_input =="1":
       display_menu()
    #checks stock of item
    elif A00[(user_input)]["stock"] == 0:
        print(f"⚠️  The {A00[(user_input)]['name']} stock has ran out, please buy another item ⚠️\n")
    
    else:
        if user_money >= A00[(user_input)]["cost"]:                                 
            user_money -= A00[(user_input)]["cost"]                                  
            A00[(user_input)]["stock"] -=1
            print(f"⚠️  Dispensed {A00[(user_input)]['name']} `(*>﹏<*)′. Remaining money {user_money}$ ⚠️\n")
        #money less then item cost
        else:
            print(f"⚠️  You do not have enough money for {A00[(user_input)]['name']}  ⚠️\n")