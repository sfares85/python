item_name = ''
item_list = []
total = 0.0
x = 0
while item_name.lower() != 'done':
	item_name = input('item (enter "done" when finished): ')
	if item_name.lower() == 'done':
		break
	item_price = float(input('price: '))
	item_quantity = int(input('quantity: '))
	item_total = item_price * item_quantity
	item_data = {"Item" : item_name, "Item price" : item_price, "Item quantity" : item_quantity , "Item total" : item_total}
	item_list.append(item_data)
	x += 1
print('-------------------\nReceipt\n-------------------')
for item in item_list:
	if x == 0:
		break
	else:
		print('%d %s %.3fKD' % (item["Item quantity"] , item["Item"] , item["Item total"]))
		total = total + item["Item total"]
		x -= 1
print('-------------------\n Total: %.3fKD \n' % total)