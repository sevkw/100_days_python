import resources

MENU = resources.MENU

def make_order(coffee):
    cost_water = MENU[coffee]["ingredients"]["water"]
    cost_milk = MENU[coffee]["ingredients"]["milk"]
    cost_coffee = MENU[coffee]["ingredients"]["coffee"]
    cost_money = MENU[coffee]["cost"]
    return cost_water, cost_milk, cost_coffee, cost_money

def insert_coin(quarter, dime, nickel, penny):
    return quarter * 0.25 + dime * 0.10 + nickel * 0.05 + penny * 0.01

def return_change(inserts, cost):
    if inserts >= cost:
        return inserts - cost

def coffee_machine():
    water = resources.resources["water"]
    milk = resources.resources["milk"]
    coffee = resources.resources["coffee"]
    machine_money = 0
    end_transaction = False

    while not end_transaction == True:
        order = input("What would you like? (espresso/latte/cappuccino): ")

        if order == "off":
            end_transaction = True
        elif order == "menu":
            print(MENU)

        elif order == "report":
            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Money: ${machine_money}")

        else:
            print("Please insert coins.")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickel = int(input("How many nickels?: "))
            penny = int(input("How many pennies?: "))
            money = insert_coin(quarter, dime, nickel, penny)
            cost_water, cost_milk, cost_coffee, cost_money  = make_order(order)


            if water >= cost_water and milk >= cost_milk and coffee >= cost_coffee and money >= cost_money:
                water -= cost_water
                milk -= cost_milk
                coffee -= cost_coffee
                machine_money += money
                change = return_change(money, cost_money)
                print(water, milk, coffee, machine_money)
                print(f"Here is ${change} in change.")
                print(f"Here is your {order}. Enjoy!")

            elif water < cost_water:
                print("Sorry not enough water.")
     
            elif milk < cost_milk:
                print("Sorry not enough milk.")
 
            elif coffee < cost_coffee:
                print("Sorry not enough coffee.")
        
            elif money < cost_money:
                print("Sorry that's not enough money. Money refunded.")

coffee_machine()