products = []

while True:
	name = input("请输入商品名称：")
	if name == "q":
		break
	price = input("请输入商品价钱： ")
	products.append([name, price])

print(products)

for product in products:
	print(product[0], "的价钱是：", product[1])