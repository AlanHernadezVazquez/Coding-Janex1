sale_price = input('Enter sale price: ')
sale_price = float(sale_price)
region =input('Enter sale region: national or foreign: ')
if (region == 'national'):
    sale_price1 = (sale_price * 1.8)
    print('The total is:',sale_price1,'euros')
elif(region == 'foreign'):
    sale_price2 = (sale_price * 1.18)
    print('The total is:',sale_price2,'euros')
