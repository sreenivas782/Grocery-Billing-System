# Grocery Billing System
from datetime import datetime

print('------WELCOME TO OUR SUPER-MARKET-----------')
name=(input('Enter your Name: '))

#LISTS of items
lists= '''
Rice    Rs 20/kg
Sugar   Rs 40/kg
Salt    Rs 35/kg
Oil     Rs 70/kg
Panner  Rs 80/kg
Maggi   Rs 50/kg
Boost   Rs 90/kg
Colgate Rs 20/kg
'''

#Declaration
price=0
pricelist=[]
totalprice=0
finalamount=0
ilist=[] #Item list
qlist=[]#quantity list
plist=[]

#rates for items

items={'Rice':20,
'Sugar':40,
'Salt':35,
'Oil':70,
'Panner':80,
'Maggi':50,
'Boosrt':90,
'Colgate':20}

#options
option=int(input('For List of Items press 1:'))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input('If you want to buy please press 1 or Press 2 to exit:'))
    if inp1==2:
        break
    if inp1==1:
        item=input('Enter your items:')
        quantity=int(input('Enter quantity:'))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price)) #as tupple
            totalprice=totalprice+price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else :
            print('Sorry you entered item is not avalible')

    else:
        print('You press wrong number')

    inp=input('Do you want bill yes/no:')
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*'=', 'SUPER MARKET',25*'=')
            print('Name:',name,30*' ',datetime.now())
            print(75*'-')
            print('s-no:',8*' ','items',8*' ','quantity',3*' ','price')
            for i in range(len(pricelist)):
                print(i,8*' ',5* ' ' ,ilist[i],3*' ',qlist[i],8*' ',plist[i])
            print(75*'-')
            print(50*' ','TotalAmount:','Rs',totalprice)
            print('GstAmount:',40*' ','Rs' ,gst)
            print(75*'-')
            print(50*'-','FinalAmount:','Rs',finalamount)
            print(75*'-')
            print(20*'-','Thanks For Visiting Our Store')
            print(75*'*')