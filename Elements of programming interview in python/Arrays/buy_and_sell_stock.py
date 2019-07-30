def buy_and_sell_stock_once(prices):

	min_price = float('inf')
	max_profit = 0

	for price in prices:

		compare_profit = price - min_price

		min_price = min(price,min_price)
		max_profit = max(max_profit,compare_profit)

	return max_profit

print(buy_and_sell_stock_once([310,315,275,295,260,270,290,230,255,250]))