products = []
while True:
    name = input('商品名稱：')
    if name == 'q':
        break
    price  = input('商品價格：')
    products.append([name, price])
print(products)

for p in products:
    print(p[0], '的價格', p[1])


with open('products.csv', 'w', encoding = 'utf-8') as f:
    # 在還沒輸入東西前 先寫入欄位名稱
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')
       


