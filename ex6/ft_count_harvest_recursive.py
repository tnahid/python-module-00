def	ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	recursive(days)
	print("Harvest time!")

def	recursive(days):
	if (days > 0):
		recursive(days - 1)
	print("Day", days)
