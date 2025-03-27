import datetime

name=input("Enter your name:")

lists='''
Rice      Rs 40/kg
sugar     Rs 25/kg
oil       Rs 45/kg
paneer    Rs 55/kg
milk      Rs/35/liter
Bread     Rs 45/pack
watermelon  Rs 30/kg
apples      Rs 55/kg
maggie      Rs 20/pack
'''
#Declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
plist=[]
qlist=[]

items={'rice':40,'sugar':25,'oil':45,'paneer':55,'milk':35,'bread':45,'watermelon':30,'apples':55,'maggie':20}
while True:
    option=input("Press 1 for list or press 2 for Exit:")
    if option =='2':
        print("Thank you for shopping.")
        break
    elif option=='1':
        print(lists)

        while True:
            display=input("To buy items press 1 or press 2 for Exit:")
            if display=='2':
                print("Thank you for shopping.")
                break
            elif display=='1':
                item=input("enter your item.:").lower()

                while True:
                    quantity_input=input("Enter your quantity:")
                    if quantity_input.isdigit():
                        quantity=int(quantity_input)
                        break
                    else:
                        print("plese enter a valid quantity:")
            if item in items:
                price= quantity * items[item]
                pricelist.append((item,price,quantity,items[item]))
                totalprice +=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
            else:
                print("Selected item is not avaliable.Choose another item in the lists.")
        if totalprice > 0:
            tax=(totalprice * 12)/100
            finalamount=tax + totalprice

            print(25 *"=","Welcome to pythonlife supermarket",25 *"=")
            print(30 *" ","Hyderabad",28 *" ")
            print("Date:",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print("Name:",name,30 *" ")
            print(75 *"-")
            print("Sno",10*" ",'Items', 8 *" ",'Quantity',8 * " ",'Price')
            for i in range(len(pricelist)):
                print(i+1,10 *" ",ilist[i],12 * " ",qlist[i],12 * " ",plist[i])
            print(75 * "-")
            print(50 * " ",'Totalamount:','Rs',totalprice)
            print("Taxamount:",52 * " ",'Rs',tax)
            print(75 *"-")
            print(50 *" ",'Finalamount:','Rs',finalamount)
            print(75 *"-")
            print(20 *" ","Thank you & Visit again",20 *" ")
            print(75 *"-")


                

              








                



