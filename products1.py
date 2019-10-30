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

with open("products2.csv","w", encoding = "gb2312") as f:
	f.write("商品,价格\n")
	for p in products:
		f.write(p[0] + "," + p[1] + "\n")