num=int(input("Enter the number of items: "))

def discount(prices_dict, quantities_dict):
    total = 0
    for i in prices_dict:
        total += prices_dict[i] * quantities_dict[i]
    if total>500:
        print("Your total is",total,". You are eligible for discount of 10%")
        print("Your final price is: ",total*0.9)
    else:
        print("Your total is: ",total)
name={}
quant={}
price={}        
for i in range(0, num):
    
    nm=input("Enter name of the item: ")
    name.update({i:nm})
    qt=int(input("Enter the quantity of the item: "))
    quant.update({i:qt})
    pr=float(input("Enter the price of the item: "))
    price.update({i:pr})

discount(price,quant)