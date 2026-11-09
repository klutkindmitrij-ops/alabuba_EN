# logistics operations

def discount(price, percent):
    if percent < 0 or percent > 100:
     print("Enter a percentage from 0 to 100 !")
     return
    discount = price / 100 * percent
    result = price - discount
    print(f"There will be a discounted item: {int(result)}")
    return result

def all_products(product, full):
      product *= full
      print(f"The total for all items is: {int(product)} dollars")
      return product

def average_amount(lis):
      if not isinstance(lis,list):
       print("Enter as a list!")
       return
      result = sum(lis) / len(lis)
      print(f"Average transaction value per item: {round(result,2)} dollars")
      return lis

def profitability(all,all_salaries, all_products):
    result = all - (all_salaries + all_products)
    print(f"Monthly total (including employee wages and product prices): {result} dollars")
    if result <= 0:
     minus = (all_salaries + all_products) - all
     print(f"You went into the minus {minus} dollars")
    return result

# Логистика и склад
def sorting_goods(list_goods, x):
 if not isinstance(list_goods, list):
        print("Enter as a list containing dictionaries.")
        return
 sorted_price = sorted(list_goods, key=lambda x: x["price"], reverse=True)
 sorted_kol = sorted(list_goods, key=lambda x: x["kol"], reverse=True)
 sorted_data = sorted(list_goods, key=lambda x: x["date"], reverse=True)
 if x == "price":
  print("Sort by price:")
  for product in sorted_price:
   print(f"{product["price"]} рублей")
 if x == "kol":
  print("Sort by kol:")
  for product in sorted_kol:
   print(f"{product["kol"]} товаров")
 if x == "date":
  print("Sort by date:")
  for product in sorted_data:
   print(f"{product["date"]}")
 if x == "all":
  print("Sort by price:")
  for product in sorted_price:
   print(f"{product["price"]} рублей")
  print("Sort by kol:") 
  for product in sorted_kol:
   print(f"{product["kol"]} товаров")
  print("Sort by date:")
  for product in sorted_data:
   print(f"{product["date"]}")
 return sorted_price,sorted_kol,sorted_data

def residue_filter(list_goods, remains, name):
    if not isinstance(list_goods,list):
            print("Enter as a list containing dictionaries.")
            return
    if name == "kol":
         print(f"List of products with a certain quantity condition ({remains}): {[int(x["kol"]) for x in list_goods if int(x["kol"]) <= int(remains)]}")
         return
    if name == "price":
         print(f"List of products with a specific price condition ({remains}): {[int(x["price"]) for x in list_goods if int(x["price"]) <= int(remains)]}")
         return

# Клиенты и сотрудники
def find_client(clients, name):
    if not isinstance(clients, list):
        print("Enter as a list containing dictionaries.")
        return 
    for client in clients:
        if client["name"] == name:
            return client
    return None

def salary_with_bonus(salary, proc):
    if proc < 0 or proc > 100:
         print("Enter a percentage from 0 to 100 !")
         return
    x = salary / 100
    proc *= x
    total = salary + proc
    print(f"Employee's salary with bonus ({proc} %) equal: {total} dollars")
    return total