import pandas as pd

def cheque(price_list, **shopping_list):
    data = []
    for product, number in shopping_list.items():
        if product in price_list:
            price = price_list[product]
            cost = price*number
            data.append((product, price, number, cost))
    cheque_df = pd.DataFrame(data, columns=['product', 'price', 'number', 'cost'])
    cheque_df = cheque_df.sort_values(by = 'product').reset_index(drop = True)
    return cheque_df

def discount(input_cheque):
    discount_cheque = input_cheque.copy()
    discount_cheque['cost'] = discount_cheque['cost'].astype('float')
    discount_cheque.loc[discount_cheque['number'] > 2, ['cost']]*=0.5
    return discount_cheque

products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda = 3, milk = 2, cream = 1)
with_discount = discount(result)
print(result)
print(with_discount)
