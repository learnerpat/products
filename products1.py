import os

products = []
if os.path.isfile("products2.csv"): #检查档案是否存在
	print("找到档案了!")
	with open("products2.csv", "r", encoding = "gb2312") as f:
		for line in f:
			if "商品,价格" in line:
				continue
			name, price = line.strip().split(",")
			products.append([name, price])
	print(products)
else:
	print("找不到档案.")

#让使用者输入
while True:
	name = input("请输入商品名称：")
	if name == "q":
		break
	price = input("请输入商品价钱： ")
	products.append([name, price])
print(products)
#印出所有购买记录
for product in products:
	print(product[0], "的价钱是：", product[1])
#写入档案
with open("products2.csv","w", encoding = "gb2312") as f:
	f.write("商品,价格\n")
	for p in products:
		f.write(p[0] + "," + p[1] + "\n")