products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}
def get_product(code):
    return products[code]
get_product("dalgona")
def get_property(code,property):
    return products[code][property]
get_property("dalgona","name")
def main():
    quantity=0
    quantity2=0
    quantity3=0
    quantity4=0
    quantity5=0
    quantity6=0
    sumtotal=0
    receipt=set()
    newlist=[]
    while(True):
        order=input("What is the customer's order?")
        if order=="/":
            break
        else:
            newlist.append(order.split(","))
            code=int(order.split(",")[1])
            receipt.add(order.split(",")[0])
            if order.split(",")[0]=="americano":
                quantity+=code
                
            elif order.split(",")[0]=="brewedcoffee":
                quantity2+=code
                    
            elif order.split(",")[0]=="cappuccino":
                quantity3+=code
                    
            elif order.split(",")[0]=="dalgona":
                quantity4+=code
                    
            elif order.split(",")[0]=="espresso":
                quantity5+=code
                    
            elif order.split(",")[0]=="frappuccino":
                quantity6+=code
    products["americano"]["quantity"]=quantity
    products["brewedcoffee"]["quantity"]=quantity2
    products["cappuccino"]["quantity"]=quantity3
    products["dalgona"]["quantity"]=quantity4
    products["espresso"]["quantity"]=quantity5
    products["frappuccino"]["quantity"]=quantity6
    receipt=sorted(receipt)
    with open("receipt.txt","w") as f:
        f.write('''
    ==
    CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
    ''')
        for x in receipt:
            f.write(f'''\t\t{x}\t\t{products[x]["name"]}\t\t{products[x]["quantity"]}\t\t\t\t{products[x]["quantity"]*products[x]["price"]}
            ''')
            sumtotal+=products[x]["quantity"]*products[x]["price"]
        f.write(f'''Total:\t\t\t\t\t\t\t\t\t\t{sumtotal}
    ==
    ''')
    
main()