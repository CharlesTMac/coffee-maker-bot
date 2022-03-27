import csv
import order

order_list = order.total_customer_orders
fields = ['Drink Number', 'Drink Size','Drink Type']

with open('total_orders.csv', 'w') as order_file:
  order_instance = csv.DictWriter(order_file, fieldnames=fields)

  order_instance.writeheader()
  for customer_dict in order_list:
    order_instance.writerow(customer_dict)

#with open('total_orders.csv',  newline='') as orders_file:
 # orders_file = csv.DictReader(orders_file)
  #for row in orders_file:
   # print(row)
   # date_list.append(row['Date'])
#print(date_list)