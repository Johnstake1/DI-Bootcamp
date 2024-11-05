#Daily Challenge
#EX1
# word = input('Give me a word')

# dictionary = {}

# for i,each_letter in enumerate(word):
#     if each_letter in dictionary:
#         dictionary[each_letter].append(i)
#     else:
#         dictionary[each_letter] = [i]
# print(dictionary)

#EX2

#Case 1

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"}

wallet = "$300"
new_wallet = int(wallet.replace("$","").replace(",",""))

print(new_wallet)
print(type(new_wallet))

converted_prices ={} # create a dictionary where to store the converted prices from strings to numbers

for item, price in items_purchase.items():
    converted_prices[item] = price.replace("$","").replace(",","")
    

print(converted_prices)

integer_prices = {}

for item, price in converted_prices.items():
    integer_prices[item] = int(price)

print(integer_prices)

aff_items = []

for item, price in converted_prices.items():
    if price <= new_wallet:
        aff_items.append(item)
print(aff_items)