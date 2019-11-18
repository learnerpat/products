import os
def read_file(filename):
    products = []
    with open(filename, "r", encoding = "gb2312") as f:
        for line in f:
            if "商品,价格" in line:
                continue
            name, price = line.strip().split(",")
            products.append([name, price])
    return products    

#让使用者输入
def user_input(products):
    while True:
        name = input("请输入商品名称：")
        if name == "q":
            break
        price = input("请输入商品价钱： ")
        products.append([name, price])
    print(products)
    return products
#印出所有购买记录 
def print_products(products):
    for product in products:
        print(product[0], "的价钱是：", product[1])
#写入档案
def write_file(filename, products):
    with open(filename,"w", encoding = "gb2312") as f:
        f.write("商品,价格\n")
        for p in products:
            f.write(p[0] + "," + p[1] + "\n")

def main():
    filename = "products2.csv"
    if os.path.isfile(filename):
        print("yeah! Find the file!")
        products = read_file(filename)
    else:
        print("找不到档案.")
    products = user_input(products)
    print_products(products)
    write_file("products2.csv", products) 

main()
