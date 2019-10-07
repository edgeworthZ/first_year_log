def usd2thb(usd):
    thb = usd*rate
    return thb

rate = float(input('Input exchange rate: '))
usd = int(input('Input USD: '))
thb = usd2thb(usd)
print(f'You get {thb:.2f} Thai Bath for {usd} USD')
