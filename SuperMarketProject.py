import math
from datetime import datetime
Customer_name = input('Enter Customer Name:')
def bill_cal():
    a = True
    Total_Price = 0
    List_of_Items = []
    while a:
        print('''
          1. list of items
          2. Choose items
          3.exit               
        ''')
        choice = int(input('Enter your Choice:'))
        choices = [1,2,3]
        if choice in choices:
            d = {'dal':60,'Biscut':25,'suger':40,'Chips':30,'Tea':50,'Coffe':40}
            if choice ==1:
                c=1
                for i,j in d.items():
                    print('\t',c,'.',i,'₹',j)
                    c+=1
            if choice ==2:
                q = True
                while q:
                    print('Press q to return main menu')
                    item = input('Entre Item:')
                    if item in d.keys():
                        qnt = input('Enter Quantity:')
                        if qnt.isdigit():
                            qnt = int(qnt)
                            price = float(d[item]*qnt)
                            List_of_Items.append((item,qnt,price))
                            Total_Price +=price
                        else:
                            print('Invalid Quantity...')
                    elif item =='q':
                        q = False
                    else:
                        print('Item Not Presented')
            if choice ==3:
                a = False
        else:
            print('Invalide Input.... Please Enter Correctly')
    return Total_Price,'Thanks You, Please Visit again...',List_of_Items

total,msg,item_price = bill_cal()
if total !=0:
    print('\n')
    print('''
                 GM Stores
             Nizampet, Hyderabad,500090
        ''')
    print('Customer Name:',Customer_name,'\t','Date:',datetime.now())
    print(20*'==')
    for j in item_price:
        print('Item:',j[0],'\tQuantity:',j[1],'Price:',j[2])
    gst = total*0.01
    gst = math.ceil(gst)
    print(18*'==')
    print('GST: Rs',float(gst))
    print('Total Payble Amount:',float(gst+total))
    print(18*'==')
    print('👏👏👏',msg,'👏👏👏')

else:
    print("Hey you did'nt bought any thing for you, get some thing for you")
    bill_cal()





