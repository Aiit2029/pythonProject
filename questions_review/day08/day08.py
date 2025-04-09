
with open('a1.txt',"r",encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        name,price,amount = line.split(' ')
        price = int(price)
        amount = int(amount)
        print({"name":name,"price":price,"amount":amount})


    

    


