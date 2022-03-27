total_customer_orders = []

def store_order(number, size, type_drink):
  customer_order_dict = {}
  customer_order_dict['Drink Number'] = number  
  customer_order_dict['Drink Type'] = type_drink
  customer_order_dict['Drink Size'] = size
    
  return customer_order_dict

def print_message():
  return "I'm sorry I did not understand your selection. Please select one of the options listed below"

def drink_type():
  order_drink = input("What kind of drink would you like to order?\n[1] Brewed coffee\n[2] Mocha\n[3] Latte\n> ")
  if order_drink == "1":
    return "Brewed Coffee"
  elif order_drink == "2":
    return "Mocha"
  elif order_drink == "3":
    return "Latte"
  else:
    print("Please select a valid option")
    return drink_type()

def drink_number():
  num_drinks = input("How many drinks would you like to order?\n> ")
  return num_drinks

def drink_size():
  size = input("What size drink would you like to order?\n[1] Small\n[2] Medium\n[3] Large\n> ")
  if size == "1":
    return "Small"
  elif size == "2":
    return "Medium"
  elif size == "3":
    return "Large"
  else:
    print_message()
    return drink_size

def take_order():
  print("Kanyi's Koffee. Can I please take your order.")
  another_order = 'y'
  while another_order == 'y':
    number = drink_number()
    size = drink_size()
    type_drink = drink_type()
    print("That will be {number} {size} {drink_type}/(s)".format(number=number, size=size, drink_type=type_drink))
    total_customer_orders.append(store_order(number, size, type_drink))

    another_order = input("Would you like to place another order?[Y/N)\n> ").lower()
    if another_order == 'n':
      print()
      print('Your orders: ')
      for customer_dict in total_customer_orders:
        print("{number} {size} {drink_type}/(s)".format(number=customer_dict['Drink Number'], size=customer_dict['Drink Size'], drink_type=customer_dict['Drink Type']))

      print('Your order will be made shortly. Thank you.')

take_order()