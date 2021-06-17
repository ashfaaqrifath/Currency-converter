amount = int(input('''Copyright © 2021 Ashfaaq Rifath
CURRENCY CONVERTER.lk
---------------------
Please enter amount(LKR): '''))
con_currency = input("Please enter convert currency: ")
if con_currency.upper() == "USD":
    converted = amount * 200
    print(f"🛑🛑🛑 {amount} LKR is {converted} 💲")
if con_currency.upper() == "EUR":
    converted = amount * 239
    print(f"🛑🛑🛑 {amount} LKR is {converted} EUR")
if con_currency.upper() == "GBP":
    converted = amount * 280
    print(f"🔴🔴🔴 {amount} LKR is {converted} GBP")


