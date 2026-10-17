# logistics operations

def discount(price,percent):
    discount = price / 100 * percent
    result = price - discount
    print(f"There will be a discounted item: {int(result)}")
    return result

def all_products(product,full):
      product *= full
      print(f"The total for all items is: {int(product)} dollars")
      return product

def average_amount(lis):
      if not isinstance(lis,list):
       print("Enter as a list!")
       return
      result = sum(lis) / len(lis)
      print(f"Average transaction value per item: {int(result)} dollars")
      return lis

def profitability(all,all_salaries,all_products):
    result = all - (all_salaries + all_products)
    print(f"Monthly total (including employee wages and product prices): {result} dollars")
    if result <= 0:
     minus = (all_salaries + all_products) - all
     print(f"You went into the minus {minus} dollars")
    return result

# Логистика и склад
def sorting_goods(list_goods):
 if not isinstance(list_goods,list):
        print("Enter as a list containing dictionaries.")
        return
 sorted_price = sorted(list_goods, key=lambda x: x["price"],reverse=True)
 sorted_kol = sorted(list_goods, key=lambda x: x["kol"],reverse=True)
 sorted_data = sorted(list_goods, key=lambda x: x["date"],reverse=True)
 print("Sort by price:")
 for product in sorted_price:
     print(f"{product["price"]} dollars")
 print("---")
 print("Sort by quantity")
 for product in sorted_kol:
     print(f"{product["kol"]} товаров")
 print("---")
 print("Sort by date")
 for product in sorted_data:
      print(f"{product["date"]}")
 return sorted_price,sorted_kol,sorted_data

def residue_filter(list_goods,remains):
    if not isinstance(list_goods,list):
            print("Enter as a list containing dictionaries.")
            return
    print(f"List of products with a certain quantity of products ({remains}):{[int(x["kol"]) for x in list_goods if int(x["kol"]) <= int(remains)]}")
    return

# Клиенты и сотрудники
def find_client(clients,name):
    if not isinstance(clients,list):
        print("Enter as a list containing dictionaries.")
        return 
    for client in clients:
        if client["name"] == name:
            return client
    return None

def salary_with_bonus(salary, proc):
    x = salary / 100
    proc *= x
    total = salary + proc
    print(f"Employee's salary with bonus ({proc} %) equal: {total} dollars")
    return total