# Логические операции
def calculator_tax(salary):
    percent = salary / 100 * 13
    result = salary - percent
    print(f"Зарплата работника с налогом, равна: {int(result)} рублей")
    return result

def discount(price, percent):
    if percent < 0 or percent > 100:
         print("Введите проценты от 0 до 100 !")
         return
    discount = price / 100 * percent
    result = price - discount
    print(f"Товар со скидкой будет: {int(result)}")
    return result

def all_products(product, full):
      product *= full
      print(f"Сумма за все товары, равна: {int(product)} рублей")
      return product

def average_amount(lis):
      if not isinstance(lis, list):
       print("Введите в виде списка!")
       return
      result = sum(lis) / len(lis)
      print(f"Средний чек за товар: {round(result,2)} рублей")
      return lis

def profitability(all,all_salaries, all_products):
    result = all - (all_salaries + all_products)
    print(f"Итог за месяц(включая зарплату работников и цены на товары): {result} рублей")
    if result <= 0:
     minus = (all_salaries + all_products) - all
     print(f"Вы ушли в минус на {minus} рублей")
    return result

# Логистика и склад
def sorting_goods(list_goods):
 if not isinstance(list_goods, list):
        print("Введите в виде списка, в котором будут словари!")
        return
 sorted_price = sorted(list_goods, key=lambda x: x["price"], reverse=True)
 sorted_kol = sorted(list_goods, key=lambda x: x["kol"], reverse=True)
 sorted_data = sorted(list_goods, key=lambda x: x["date"], reverse=True)
 print("Сортировка по цене:")
 for product in sorted_price:
     print(f"{product["price"]} рублей")
 print("---")
 print("Сортировка по количеству")
 for product in sorted_kol:
     print(f"{product["kol"]} товаров")
 print("---")
 print("Сортировка по дате")
 for product in sorted_data:
      print(f"{product["date"]}")
 return sorted_price,sorted_kol,sorted_data

def residue_filter(list_goods, remains, name):
    if not isinstance(list_goods, list):
            print("Введите в виде списка, в котором будут словари!")
            return
    if name == "kol":
     print(f"Список товаров с определененым условием количества ({remains}): {[int(x["kol"]) for x in list_goods if int(x["kol"]) <= int(remains)]}")
     return
    if name == "price":
     print(f"Список товаров с определененым условием цены ({remains}): {[int(x["price"]) for x in list_goods if int(x["price"]) <= int(remains)]}")
     return

# Клиенты и сотрудники
def find_client(clients, name):
    if not isinstance(clients,list):
        print("Введите в виде списка, в котором будут словари!")
        return 
    for client in clients:
        if client["name"] == name:
            return client
    return None

def salary_with_bonus(salary, proc):
    if proc < 0 or proc > 100:
     print("Введите проценты от 0 до 100 !")
     return
    x = salary / 100
    proc *= x
    total = salary + proc
    print(f"Зарплата работника, с премией равна: {int(total)} рублей")
    return total