stock = []
while True:
    product_name = input('Для добавления нового товара введите его имя. Для выхода нажмите "Q":')
    if product_name == "Q":
        break
    product_price = input(f'Укажите стоимость товара {product_name}:')
    product_count = input(f'Укажите количество товара {product_name}:')
    product_unit = input(f'Укажите единицу измерения товара {product_name}:')
    stock.append((len(stock)+1, {'name': product_name, 'price': product_price,
                                 'count': product_count, 'unit': product_unit}))
    print(stock)
analytics = {'name': set(), 'price': set(), 'count': set(), 'unit': set()}
for i in stock:
    analytics.get('name').add(i[1].get('name'))
    analytics.get('price').add(i[1].get('price'))
    analytics.get('count').add(i[1].get('count'))
    analytics.get('unit').add(i[1].get('unit'))
print(analytics)
