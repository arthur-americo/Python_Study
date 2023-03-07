'''Create a program that has a single tuple with product names and their respective prices, in sequence. At the end, 
show a price list, organizing the data in tabular form.'''
product_names = ('Pencil', 'Eraser', 'Notebook', 'Pen', 'Ruler', 'Compass', 'Pencil case', 'Backpack', 'Calculator', 'Stapler')
prices = (1.75, 2, 15.90, 4.20, 3.50, 9.99, 25, 120, 42.30, 9.08)
price_list = ('Price List',)
for i in range(0, len(product_names)):
    price_list += (product_names[i], prices[i])
print(f'{price_list[0]:.<30}')
print('-' * 30)
for i in range(1, len(price_list), 2):
    print(f'{price_list[i]:.<30}R${price_list[i + 1]:>7.2f}')
    

