price = 1000000
g_cred=True

if g_cred:
    price = 0.1*price
else:
    price = 0.2*price
print(f'Down payment: ${price}')