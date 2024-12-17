def input_store_names(num_stores):
    store_names = []
    for i in range(num_stores):
        name = input(f"Введите название магазина {i+1}: ")
        store_names.append(name)
    return store_names

def input_prices(store_names, num_products):
    prices = {}
    for i in range(num_products):
        product_name = input(f"Введите название товара {i+1}: ")
        prices[product_name] = []
        for store_name in store_names:
            price = float(input(f"Введите цену в магазине '{store_name}' для {product_name}: "))
            prices[product_name].append(price)
    return prices

def calculate_costs(prices):
    total_costs = [0] * len(prices[next(iter(prices))])
    for price_list in prices.values():
        for i, price in enumerate(price_list):
            total_costs[i] += price
    return total_costs

def find_cheapest_store(store_names, total_costs):
    min_cost = min(total_costs)
    min_index = total_costs.index(min_cost)
    return store_names[min_index], min_cost



num_stores = int(input("Введите количество магазинов: "))
store_names = input_store_names(num_stores)
num_products = int(input("Введите количество товаров: "))

prices = input_prices(store_names, num_products)
total_costs = calculate_costs(prices)
cheapest_store, min_cost = find_cheapest_store(store_names, total_costs)

# Вывод результатов
print("\nСумма чека в магазинах:")
for store_name, cost in zip(store_names, total_costs):
    print(f"{store_name}: {cost} руб.")
print(f"\nДешевле закупиться будет в : {cheapest_store} (Стоимость: {min_cost} руб.)")
